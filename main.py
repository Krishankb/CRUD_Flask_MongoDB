from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
import bson


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['library'] 

collection = db['books']  


@app.route('/books', methods=['GET'])
def get_books():
    books = list(collection.find())
    for book in books:
        book['_id'] = str(book['_id'])
    return jsonify(books), 200

@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    try:
        book = collection.find_one({'_id': str(id)})
        if book:
            return jsonify(book), 200
        else:
            return jsonify({'message': 'Book not found'}), 404
    except bson.errors.InvalidId:
        return jsonify({'message': 'Invalid book ID'}), 400

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({'message': 'book created successfully'}), 201

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    result = collection.update_one({'_id': str(id)}, {'$set': data})
    if result.modified_count > 0:
        return jsonify({'message': 'book updated successfully'}), 200
    else:
        return jsonify({'message': 'book not found'}), 404

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    result = collection.delete_one({'_id': ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'book deleted successfully'}), 200
    else:
        return jsonify({'message': 'book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
