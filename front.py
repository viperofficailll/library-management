import tkinter as tk
from tkinter import messagebox


class LibraryManagementSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.label_title = tk.Label(root, text="Library Management System", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.label_book_id = tk.Label(root, text="Book ID:")
        self.label_book_id.pack()
        self.entry_book_id = tk.Entry(root)
        self.entry_book_id.pack()

        self.label_title = tk.Label(root, text="Title:")
        self.label_title.pack()
        self.entry_title = tk.Entry(root)
        self.entry_title.pack()

        self.label_author = tk.Label(root, text="Author:")
        self.label_author.pack()
        self.entry_author = tk.Entry(root)
        self.entry_author.pack()

        self.button_add_book = tk.Button(root, text="Add Book", command=self.add_book)
        self.button_add_book.pack(pady=10)

        self.button_remove_book = tk.Button(root, text="Remove Book", command=self.remove_book)
        self.button_remove_book.pack(pady=10)

        self.button_display_books = tk.Button(root, text="Display Books", command=self.display_books)
        self.button_display_books.pack(pady=10)

        self.button_lend_book = tk.Button(root, text="Lend Book", command=self.lend_book)
        self.button_lend_book.pack(pady=10)

        self.button_return_book = tk.Button(root, text="Return Book", command=self.return_book)
        self.button_return_book.pack(pady=10)

    def add_book(self):
        book_id = self.entry_book_id.get()
        title = self.entry_title.get()
        author = self.entry_author.get()

        # Perform backend operation to add book
        # library.add_book(book_id, title, author)

        messagebox.showinfo("Book Added", "Book added successfully.")

    def remove_book(self):
        book_id = self.entry_book_id.get()

        # Perform backend operation to remove book
        # library.remove_book(book_id)

        messagebox.showinfo("Book Removed", "Book removed successfully.")

    def display_books(self):
        # Perform backend operation to display books
        # books = library.get_books()

        # Create a new window to display books
        books_window = tk.Toplevel(self.root)
        books_window.title("Books")

        label_books = tk.Label(books_window, text="Books in the library:")
        label_books.pack(pady=10)

        # Display each book in the window
        # for book in books:
        #     label = tk.Label(books_window, text=f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        #     label.pack()

    def lend_book(self):
        book_id = self.entry_book_id.get()

        # Perform backend operation to lend book
        # library.lend_book(book_id)

        messagebox.showinfo("Book Lent", "Book lent successfully.")

    def return_book(self):
        book_id = self.entry_book_id.get()

        # Perform backend operation to return book
        # library.return_book(book_id)

        messagebox.showinfo("Book Returned", "Book returned successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementSystemGUI(root)
    root.mainloop()