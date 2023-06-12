from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample book data
books = [
    {'id': 1, 'title': 'Book 1', 'author': 'Author 1'},
    {'id': 2, 'title': 'Book 2', 'author': 'Author 2'},
]


# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200


# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201


# Route to search for books by title
@app.route('/books', methods=['GET'])
def search_books():
    title = request.args.get('title')
    search_results = [book for book in books if title.lower() in book['title'].lower()]
    return jsonify(search_results), 200


# Route to delete a book by its ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return '', 204
    return jsonify({'error': 'Book not found'}), 404


# Route to update a book's details
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book['title'] = data['title']
            book['author'] = data['author']
            return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404


# Run the backend server
if __name__ == '__main__':
    app.run()