# Book-Library

This is book library application. It allows you to keep track of the books that you are reading or going to read. The application opens with a menu for the user to interact with.

#### Additional info
I used it to keep track of my text books when studying for subjects at university. The application handles errors such as menu input handling and checking if a book(s) exists before updating, deleting or displaying and more. It also handles unique book names, meaning that no two books are allowed to have the same name. 
Components/functions do not heavily rely on one another. as such, coupling is kept low. A context manager is also built to open and close connections to the database. It uses SQLite3 for database CRUD operations
because it is lightweight and there is only one user writing and reading to and from the database for the lifetime of the application.

#### Technologies used:
- Python (Programming Language)
- Pycharm (IDE)
- SQLite3 (Database)

#### What the application offers:
- Add a book
- Update the 'read' status 
- Display all the books
- Delete a book
