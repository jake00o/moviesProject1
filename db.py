"""Database module for the movie list app."""
import sqlite3
from object import Movie, Category

def connect():
    """Connect to the SQLite database."""
    try:
        return sqlite3.connect('movies.db')
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        raise

def close(conn):
    """Close the database connection."""
    try:
        conn.close()
    except sqlite3.Error as e:
        print("Error closing connection:", e)
        raise

def initialize_db(conn):
    """Initialize the database with tables and sample data."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                year INTEGER,
                minutes INTEGER,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM categories")
        if cursor.fetchone()[0] == 0:
            categories = [("Anime",), ("DC Movies",), ("Marvel movies",)]
            cursor.executemany("INSERT INTO categories (name) VALUES (?)", categories)
            conn.commit()
        cursor.execute("SELECT COUNT(*) FROM movies")
        if cursor.fetchone()[0] == 0:
            cursor.execute("SELECT id, name FROM categories")
            cat_dict = {name: id for id, name in cursor.fetchall()}
            anime_movies = [
                ("Spirited Away", 2001, 125, cat_dict["Anime"]),
                ("Akira", 1988, 124, cat_dict["Anime"]),
                ("Ghost in the Shell", 1995, 83, cat_dict["Anime"]),
                ("Princess Mononoke", 1997, 134, cat_dict["Anime"]),
                ("My Neighbor Totoro", 1988, 86, cat_dict["Anime"]),
                ("Your Name", 2016, 106, cat_dict["Anime"]),
                ("Perfect Blue", 1997, 81, cat_dict["Anime"]),
                ("The Girl Who Leapt Through Time", 2006, 98, cat_dict["Anime"]),
                ("5 Centimeters per Second", 2007, 63, cat_dict["Anime"]),
                ("Weathering with You", 2019, 112, cat_dict["Anime"])
            ]
            dc_movies = [
                ("Batman Begins", 2005, 140, cat_dict["DC Movies"]),
                ("The Dark Knight", 2008, 152, cat_dict["DC Movies"]),
                ("Man of Steel", 2013, 143, cat_dict["DC Movies"]),
                ("Wonder Woman", 2017, 141, cat_dict["DC Movies"]),
                ("Aquaman", 2018, 143, cat_dict["DC Movies"]),
                ("Shazam!", 2019, 132, cat_dict["DC Movies"]),
                ("Joker", 2019, 122, cat_dict["DC Movies"]),
                ("Justice League", 2017, 120, cat_dict["DC Movies"]),
                ("Suicide Squad", 2016, 123, cat_dict["DC Movies"]),
                ("The Batman", 2022, 176, cat_dict["DC Movies"])
            ]
            marvel_movies = [
                ("Iron Man", 2008, 126, cat_dict["Marvel movies"]),
                ("The Incredible Hulk", 2008, 112, cat_dict["Marvel movies"]),
                ("Thor", 2011, 115, cat_dict["Marvel movies"]),
                ("Captain America: The First Avenger", 2011, 124, cat_dict["Marvel movies"]),
                ("The Avengers", 2012, 143, cat_dict["Marvel movies"]),
                ("Guardians of the Galaxy", 2014, 121, cat_dict["Marvel movies"]),
                ("Doctor Strange", 2016, 115, cat_dict["Marvel movies"]),
                ("Black Panther", 2018, 134, cat_dict["Marvel movies"]),
                ("Captain Marvel", 2019, 123, cat_dict["Marvel movies"]),
                ("Spider-Man: Homecoming", 2017, 133, cat_dict["Marvel movies"])
            ]
            sample_movies = anime_movies + dc_movies + marvel_movies
            cursor.executemany("INSERT INTO movies (name, year, minutes, category_id) VALUES (?, ?, ?, ?)", sample_movies)
            conn.commit()
    except sqlite3.Error as e:
        print("Error initializing database:", e)
        raise

def make_category(row):
    """Create a Category object from a database row."""
    try:
        return Category(id=row[0], name=row[1])
    except Exception as e:
        print("Error in make_category:", e)
        raise

def make_movie(row):
    """Create a Movie object from a database row, using make_category."""
    try:
        cat = Category(id=row[4], name=row[5])
        return Movie(id=row[0], name=row[1], year=row[2], minutes=row[3], category=cat)
    except Exception as e:
        print("Error in make_movie:", e)
        raise

def get_categories(conn):
    """Retrieve and return a list of all categories."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories")
        rows = cursor.fetchall()
        return [make_category(row) for row in rows]
    except sqlite3.Error as e:
        print("Error getting categories:", e)
        return []

def get_category(conn, category_id):
    """Retrieve and return a Category object by ID."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM categories WHERE id=?", (category_id,))
        row = cursor.fetchone()
        return make_category(row) if row else None
    except sqlite3.Error as e:
        print("Error getting category:", e)
        return None

def make_movie_list(results):
    """Create a list of Movie objects from a database result set."""
    try:
        return [make_movie(row) for row in results]
    except Exception as e:
        print("Error in make_movie_list:", e)
        return []

def get_all_movies(conn):
    """Retrieve and return a list of all movies."""
    try:
        cursor = conn.cursor()
        query = """
        SELECT m.id, m.name, m.year, m.minutes, c.id, c.name
        FROM movies m JOIN categories c ON m.category_id = c.id
        ORDER BY m.id
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return make_movie_list(rows)
    except sqlite3.Error as e:
        print("Error getting all movies:", e)
        return []

def get_movies_by_category(conn, category_id):
    """Retrieve and return a list of Movie objects for a given category ID."""
    try:
        cursor = conn.cursor()
        query = """
        SELECT m.id, m.name, m.year, m.minutes, c.id, c.name
        FROM movies m JOIN categories c ON m.category_id = c.id
        WHERE c.id = ?
        ORDER BY m.id
        """
        cursor.execute(query, (category_id,))
        rows = cursor.fetchall()
        return make_movie_list(rows)
    except sqlite3.Error as e:
        print("Error getting movies by category:", e)
        return []

def get_movies_by_year(conn, year):
    """Retrieve and return a list of Movie objects for a given year."""
    try:
        cursor = conn.cursor()
        query = """
        SELECT m.id, m.name, m.year, m.minutes, c.id, c.name
        FROM movies m JOIN categories c ON m.category_id = c.id
        WHERE m.year = ?
        ORDER BY m.id
        """
        cursor.execute(query, (year,))
        rows = cursor.fetchall()
        return make_movie_list(rows)
    except sqlite3.Error as e:
        print("Error getting movies by year:", e)
        return []

def add_movie(conn, movie):
    """Add a new movie to the database."""
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies (name, year, minutes, category_id) VALUES (?, ?, ?, ?)",
                       (movie.name, movie.year, movie.minutes, movie.category.id))
        conn.commit()
    except sqlite3.Error as e:
        print("Error adding movie:", e)

def delete_movie(conn, movie_id):
    """Delete a movie from the database by ID."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM movies WHERE id = ?", (movie_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting movie:", e)
