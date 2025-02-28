"""Main module for the movie list app."""
import time
import db
import ui

def main():
    """Main entry point of the application."""
    try:
        conn = db.connect()
        db.initialize_db(conn)
    except Exception as e:
        print("Initialization error:", e)
        return

    ui.display_welcome()
    while True:
        try:
            ui.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                ui.display_all_movies(conn)
                input("Press Enter to continue...")
            elif choice == '2':
                ui.display_categories(conn)
                input("Press Enter to continue...")
            elif choice == '3':
                ui.display_movies_by_category(conn)
            elif choice == '4':
                ui.display_movies_by_year(conn)
            elif choice == '5':
                ui.add_movie(conn)
            elif choice == '6':
                ui.delete_movie(conn)
            elif choice == '7':
                ui.display_goodbye()
                break
            else:
                print("Invalid choice.")
                time.sleep(1)
        except Exception as e:
            print("Error:", e)
    try:
        db.close(conn)
    except Exception as e:
        print("Error closing connection:", e)

if __name__ == "__main__":
    main()
