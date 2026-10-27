import argparse
import os
import sys
from .favorites import FavoritesManager
from .weather_api import WeatherAPI, format_current_weather, format_forecast


FAVORITES_FILE = 'favorites.json'


def load_api_key():
    """Load API key from env or config.py."""
    # Try environment variable first
    key = os.getenv('WEATHER_API_KEY')
    if key:
        return key
    
    # Try config.py
    try:
        from .config import WEATHER_API_KEY
        return WEATHER_API_KEY
    except ImportError:
        return None


def build_parser():
    """Build the argument parser."""
    parser = argparse.ArgumentParser(description="Weather CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # current LOCATION
    current_parser = subparsers.add_parser('current', help='Get current weather')
    current_parser.add_argument('location', help='City name or favorite name')
    
    # forecast LOCATION --days
    forecast_parser = subparsers.add_parser('forecast', help='Get forecast')
    forecast_parser.add_argument('location', help='City name or favorite name')
    forecast_parser.add_argument('--days', type=int, default=3, help='Days (1-3)')
    
    # favorites add NAME LOCATION
    favorites_parser = subparsers.add_parser('favorites', help='Manage favorites')
    fav_subparsers = favorites_parser.add_subparsers(dest='favorites_command', help='Favorite commands')
    
    add_parser = fav_subparsers.add_parser('add', help='Add favorite')
    add_parser.add_argument('name', help='Favorite name')
    add_parser.add_argument('location', help='Location')
    
    remove_parser = fav_subparsers.add_parser('remove', help='Remove favorite')
    remove_parser.add_argument('name', help='Favorite name')
    
    fav_subparsers.add_parser('list', help='List all favorites')
    
    return parser


def main(argv=None):
    """Main CLI function."""
    parser = build_parser()
    args = parser.parse_args(argv)
    
    api_key = load_api_key()
    if not api_key:
        print("Error: API key not found", file=sys.stderr)
        return 1
    
    api = WeatherAPI(api_key)
    fav_manager = FavoritesManager(FAVORITES_FILE)
    
    # Handle current weather
    if args.command == 'current':
        location = fav_manager.get_location(args.location) or args.location
        data = api.get_current_weather(location)
        if data is None:
            print("Error: Failed to fetch weather", file=sys.stderr)
            return 1
        print(format_current_weather(data))
        return 0
    
    # Handle forecast
    elif args.command == 'forecast':
        try:
            location = fav_manager.get_location(args.location) or args.location
            data = api.get_forecast(location, args.days)
            if data is None:
                print("Error: Failed to fetch forecast", file=sys.stderr)
                return 1
            result = format_forecast(data)
            if result:
                print(result)
            return 0
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    
    # Handle favorites
    elif args.command == 'favorites':
        if args.favorites_command == 'add':
            if not fav_manager.add(args.name, args.location):
                print("Error: Favorite already exists", file=sys.stderr)
                return 1
            return 0
        elif args.favorites_command == 'remove':
            if not fav_manager.remove(args.name):
                print("Error: Favorite not found", file=sys.stderr)
                return 1
            return 0
        elif args.favorites_command == 'list':
            favs = fav_manager.list_all()
            if not favs:
                print("No favorites")
                return 0
            for name, location in favs.items():
                print(f"{name}: {location}")
            return 0
    
    return 0


if __name__ == '__main__':
    sys.exit(main())