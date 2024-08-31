from datetime import datetime

# Sample book data
library_books = [
    {"title": "Book A", "author": "Author A", "checked_out": True, "due_date": "2024-08-30"},
    {"title": "Book B", "author": "Author B", "checked_out": False, "due_date": None},
    {"title": "Book C", "author": "Author C", "checked_out": True, "due_date": "2024-08-20"},
    {"title": "Book D", "author": "Author D", "checked_out": False, "due_date": None},
    {"title": "Book E", "author": "Author E", "checked_out": True, "due_date": "2024-08-25"},
]

# Function to calculate the total number of books
def total_books(data):
    return len(data)

# Function to calculate the total number of books available (not checked out)
def available_books(data):
    return sum(1 for book in data if not book["checked_out"])

# Function to list all overdue books
def overdue_books(data):
    overdue = []
    today = datetime.today().date()
    for book in data:
        if book["checked_out"] and book["due_date"]:
            due_date = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
            if due_date < today:
                overdue.append(book)
    return overdue

# Function to track the most borrowed books (for simplicity, we assume books with earlier due dates are borrowed more)
def most_borrowed_books(data):
    borrowed = sorted([book for book in data if book["checked_out"]], key=lambda x: x["due_date"])
    return borrowed

# Running the analysis
total_books_count = total_books(library_books)
available_books_count = available_books(library_books)
overdue_books_list = overdue_books(library_books)
most_borrowed_books_list = most_borrowed_books(library_books)

# Printing the results
print(f"Total Number of Books: {total_books_count}")
print(f"Total Number of Available Books: {available_books_count}")

print("\nOverdue Books:")
for book in overdue_books_list:
    print(f"  Title: {book['title']}, Due Date: {book['due_date']}")

print("\nMost Borrowed Books:")
for book in most_borrowed_books_list:
    print(f"  Title: {book['title']}, Due Date: {book['due_date']}")
