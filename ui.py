"""User interface module for the movie list app."""
import os
import time
try:
    from pyfiglet import figlet_format
except ImportError:
    def figlet_format(text, font="slant"):
        return text.upper()
from object import Movie
import db

def clear_screen():
    """Clear the terminal screen."""
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except OSError as e:
        print("Error clearing screen:", e)

def print_header():
    """Print persistent header using pyfiglet."""
    header = figlet_format("Movie List", font="slant")
    print(header)

def display_welcome():
    """Display welcome message with header and pause."""
    clear_screen()
    print_header()
    print("Welcome to the Movie List Program!")
    time.sleep(2)

def display_menu():
    """Display the main menu with persistent header."""
    clear_screen()
    print_header()
    print("Menu:")
    print("1. Display All Movies")
    print("2. Display All Categories")
    print("3. Display Movies by Category")
    print("4. Display Movies by Year")
    print("5. Add a Movie")
    print("6. Delete a Movie")
    print("7. Exit")

def display_all_movies(conn):
    """Display all movies from the database."""
    try:
        movies = db.get_all_movies(conn)
        if movies:
            print("\nAll Movies:")
            for movie in movies:
                print(movie)
        else:
            print("No movies found.")
    except Exception as e:
        print("Error displaying all movies:", e)

def display_categories(conn):
    """Display all categories."""
    try:
        categories = db.get_categories(conn)
        if categories:
            print("\nCategories:")
            for cat in categories:
                print(cat)
        else:
            print("No categories found.")
    except Exception as e:
        print("Error displaying categories:", e)

def display_movies(movies, title_term):
    """Display a list of movies with a title."""
    try:
        if movies:
            print(f"\nMovies {title_term}:")
            for movie in movies:
                print(movie)
        else:
            print(f"No movies found for {title_term}.")
    except Exception as e:
        print("Error displaying movies:", e)

def get_int(prompt):
    """Get an integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter an integer.")

def display_movies_by_category(conn):
    """Display movies filtered by category."""
    try:
        display_categories(conn)
        cat_id = get_int("Enter category id: ")
        movies = db.get_movies_by_category(conn, cat_id)
        display_movies(movies, f"for category {cat_id}")
        input("Press Enter to continue...")
    except Exception as e:
        print("Error displaying movies by category:", e)

def display_movies_by_year(conn):
    """Display movies filtered by year."""
    try:
        year = get_int("Enter movie year: ")
        movies = db.get_movies_by_year(conn, year)
        display_movies(movies, f"from year {year}")
        input("Press Enter to continue...")
    except Exception as e:
        print("Error displaying movies by year:", e)

def add_movie(conn):
    """Prompt user to add a movie to the database."""
    try:
        name = input("Enter movie name: ")
        year = get_int("Enter movie year: ")
        minutes = get_int("Enter movie duration (minutes): ")
        display_categories(conn)
        cat_id = get_int("Enter category id: ")
        category = db.get_category(conn, cat_id)
        if not category:
            print("Invalid category id.")
            time.sleep(1)
            return
        movie = Movie(name=name, year=year, minutes=minutes, category=category)
        db.add_movie(conn, movie)
        print("Movie added.")
        time.sleep(1)
    except Exception as e:
        print("Error adding movie:", e)

def delete_movie(conn):
    """Prompt user to delete a movie from the database."""
    try:
        movie_id = get_int("Enter movie id to delete: ")
        db.delete_movie(conn, movie_id)
        print("Movie deleted if existed.")
        time.sleep(1)
    except Exception as e:
        print("Error deleting movie:", e)

def display_goodbye():
    text = "Goodbye!"
    try:
        output = ""
        for char in text:
            output += char
            clear_screen()
            print(figlet_format(output, font="slant"))
            time.sleep(0.3)
    except Exception:
        print("Goodbye!")
    time.sleep(2)
