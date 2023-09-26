from utils.database_connection import DatabaseConnection
import sqlite3

"""
This file is concerned with adding, updating, storing and retrieving books from the database
"""


# Function that creates a books table
def create_books_file():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS books(name TEXT PRIMARY KEY, author TEXT, read INTEGER)')


# Funtion that adds a book to the database
# Value 0 represents false which indicates that the book has not yet been read
def add_book(book_name, author):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        try:
            # Protecting SQL insert statement from SQL injections using '?'
            cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (book_name, author))
            print(f"'{book_name}' by '{author}' successfully added!")
        except sqlite3.IntegrityError:
            print(f"~~'{book_name}' already exists~~")


# Function that displays all books
def get_all_books():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM books')

        # cursor.fetchall() returns a list of tuples -> [(name, author, read), (name, author, read), ....]
        # code below uses dictionary comprehension to convert tuples into a dictionary
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books


# Function that marks a book as 1 which means that the book has been read
def mark_book_as_read(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # Getting book row
        # 1st if statement checks if the given book exists
        # 2nd if statement checks if the given book has already been marked as finished read
        cursor.execute(f"SELECT * FROM `books` WHERE `name` = '{book_name}';")
        row = cursor.fetchall()
        if len(row) > 0:
            if row[0][2] == 1:
                print(f"'{book_name}' has already been marked as read.")
            else:
                cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (book_name,))
                print(f"'{book_name}' successfully marked as read!")
        else:
            print(f"~~'{book_name}' does not exist~~")
            print("~~Please check spelling~~")


# Function that deletes a book
def delete_book(book_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        # Getting book row
        # Checking if the length of the row is greater than 0 which means that the book exists
        cursor.execute(f"SELECT * FROM `books` WHERE `name` = '{book_name}';")
        row = cursor.fetchall()
        if len(row) > 0:
            cursor.execute('DELETE FROM books WHERE name = ?', (book_name,))
            print(f"'{book_name}' successfully deleted!")
        else:
            print(f"~~'{book_name}' does not exist~~")
            print("~~Please check spelling~~")
