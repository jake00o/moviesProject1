# Movie List Program

## Overview
This is a **Movie List Program** that allows users to **view, add, and delete movies** stored in an SQLite database. The program follows a **three-tier architecture**:
- **Object Tier (`object.py`)**: Defines `Movie` and `Category` classes.
- **Database Tier (`db.py`)**: Handles SQLite interactions.
- **Presentation Tier (`ui.py`)**: Manages user interface and input.

## Features
- View all movies
- View all categories
- Filter movies by category or year
- Add a new movie
- Delete a movie

## Installation
To run this program, you need **Python 3+** and SQLite installed on your system.

### 1. Clone the Repository
```sh
git clone https://github.com/jake00o/moviesProject1
cd movie-list-program
```

### 2. Install Dependencies
The program uses `pyfiglet` for aesthetic text formatting. It is **optional** but recommended.

**To install `pyfiglet`:**
```sh
pip install pyfiglet
```

*(If you don’t install `pyfiglet`, the program will still work, but without fancy text formatting.)*

### 3. Run the Program
```sh
python main.py
```

## File Structure
```
📂 movie-list-program
├── db.py          # Database operations
├── object.py      # Movie & Category classes
├── ui.py          # User interface
├── main.py        # Main program entry
├── movies.db      # SQLite database
├── README.md      # This file
```

## Notes
- **Ensure SQLite is installed and `movies.db` is in the same directory.**
- If you face any issues, check dependencies and try reinstalling Python packages.

## License
This project is for educational purposes. Feel free to modify and improve it!

---
**Author:** *Manjot Singh*
