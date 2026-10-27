import json
import os


class FavoritesManager:
    def __init__(self, filename):
        self.filename = filename
        self.favorites = self._load()
    
    def _load(self):
        """Load from JSON, return empty dict if file doesn't exist."""
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    
    def _save(self):
        """Write to JSON."""
        with open(self.filename, 'w') as f:
            json.dump(self.favorites, f, indent=4)
    
    def add(self, name, location):
        """Add a favorite. Return True on success, False if duplicate."""
        if name.lower() in self.favorites:
            return False
        self.favorites[name.lower()] = location
        self._save()
        return True
    
    def remove(self, name):
        """Remove a favorite. Return True on success, False if not found."""
        if name.lower() not in self.favorites:
            return False
        del self.favorites[name.lower()]
        self._save()
        return True
    
    def list_all(self):
        """Return dict of all favorites."""
        return self.favorites
    
    def get_location(self, name):
        """Get location by name, return None if not found."""
        return self.favorites.get(name.lower())