from utils import database

"""
This is the main file that holds the menu and its operations.
"""


# Main menu string that is called by input()
USER_CHOICE = """
=============================
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
=============================
Enter here: """


# Main Function that holds menu operations
def main():
    # Creating books table
    database.create_books_file()
    menu = input(USER_CHOICE).lower()
    while menu != "q":
        match menu:
            case "a":
                prompt_add_book()
            case "l":
                list_books()
            case "r":
                prompt_read_book()
            case "d":
                prompt_delete_book()
            case _:
                print("Invalid Entry. Please enter a valid command")

        menu = input(USER_CHOICE).lower()


# Funtion that prompts the user to add a book
def prompt_add_book():
    book_name = input("Book Name: ").title().strip()
    author = input("Author name: ").title().strip()

    database.add_book(book_name, author)


# Function that displays all books from the database
def list_books():
    books = database.get_all_books()
    if books:
        for book in books:
            read = 'Finished' if book['read'] else 'Not finished'   # if the read variable is 1 read = 'Finished' else read = 'Not finished'
            print(f"- {book['name']} by {book['author']}, read: {read}")
    else:
        print("~~Books database is empty~~")


# Function that prompts the user to enter the name of the book to be marked as read
def prompt_read_book():
    book_name = input("Enter the name of the book that you want to mark as read: ").title().strip()
    database.mark_book_as_read(book_name)


# Function that prompts the user to enter the name of the book to be deleted
def prompt_delete_book():
    book_name = input("Enter the name of the book that you want to delete: ").title().strip()
    database.delete_book(book_name)


# Starting application
main()
