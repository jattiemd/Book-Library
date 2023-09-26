import sqlite3

"""
This file builds a context manager for the database connection to remove repetition 
of creating the connection, committing changes and closing the connection to the database. 
"""


# Context manager class that establishes a connection with a given database file name
class DatabaseConnection:
    def __init__(self, db_file_name):
        self.connection = None
        self.db_file_name = db_file_name   # Database file name eg. 'data.db'

    # Entering the context manager
    # Opening database connection
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_file_name)
        return self.connection

    # Leaving the context manager
    # Closing database connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        # if statement closes the connection of the context manager if any exception is picked up while using the context manager
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
