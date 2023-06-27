# Library Management System  
This is a simple library management system implemented in Python. It allows users to manage a collection of books, including adding new books, deleting existing books, and purchasing books from the collection.  
## Prerequisites  
Before running the code, make sure you have the following dependencies installed:  
- Python (version 3 or above)
- `prettytable` library  
You can install the `prettytable` library using the following command:
```bash
pip install prettytable
```
## Getting Started
1. Clone or download the code repository to your local machine.
2. Navigate to the directory where the code is located.
## Usage  
1. Run the code using the following command:
```bash
python library_management.py
```
1. The program will display a menu with the following options:
  - Show Books: Display the list of available books in a tabular format.
  - Add Book: Add a new book to the collection.
  - Delete Book: Delete an existing book from the collection.
  - Purchase Book: Purchase a book from the collection.
  - Exit: Exit the program.
2. Enter the corresponding number for the desired action and follow the prompts.
## Data Storage  
The book collection and transaction history are stored in two separate text files: `data.txt` and `transaction.txt`. Ensure these files are in the same directory as the code file.  
## Notes  
- Book names are case-insensitive. However, it is recommended to use lowercase for consistency.
- The program provides a command-line interface (CLI) for interaction.
