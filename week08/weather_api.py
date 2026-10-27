import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
    
    def get_current_weather(self, location):
        """Fetch current weather, return None on error."""
        try:
            response = requests.get(
                f"{self.base_url}/current.json",
                params={"key": self.api_key, "q": location},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError):
            return None
    
    def get_forecast(self, location, days=3):
        """Fetch forecast, return None on error."""
        if days < 1 or days > 3:
            raise ValueError("Days must be between 1 and 3")
        try:
            response = requests.get(
                f"{self.base_url}/forecast.json",
                params={"key": self.api_key, "q": location, "days": days},
                timeout=10
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            if isinstance(e, ValueError) and "Days must be" in str(e):
                raise
            return None


def format_current_weather(data):
    """Format: CITY, COUNTRY: TEMP°F, CONDITION"""
    if not data:
        return None
    current = data['current']
    location = data['location']
    city = location['name']
    country = location['country']
    temp = current['temp_f']
    condition = current['condition']['text']
    return f"{city}, {country}: {temp}°F, {condition}"


def format_forecast(data):
    """Format each day as: DATE: high TEMP°F, low TEMP°F, CONDITION"""
    if not data:
        return None
    days = data['forecast']['forecastday']
    formatted_days = []
    for day in days:
        date = day['date']
        high = day['day']['maxtemp_f']
        low = day['day']['mintemp_f']
        condition = day['day']['condition']['text']
        formatted_days.append(f"{date}: high {high}°F, low {low}°F, {condition}")
    return "\n".join(formatted_days)