"""Object classes for the movie list app."""

class Category:
    def __init__(self, id=0, name=""):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}: {self.name}"

class Movie:
    def __init__(self, id=0, name="", year=2000, minutes=0, category=None):
        self.id = id
        self.name = name
        self.year = year
        self.minutes = minutes
        self.category = category

    def __str__(self):
        cat_name = self.category.name if self.category else "Unknown"
        return f"{self.id} - {self.name} ({self.year}) [{self.minutes} mins, Category: {cat_name}]"
