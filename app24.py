from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Book One"},
    {"id": 2, "title": "Book Two"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    books.append(data)
    return jsonify(data), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    for book in books:
        if book["id"] == id:
            book.update(request.json)
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [b for b in books if b["id"] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
