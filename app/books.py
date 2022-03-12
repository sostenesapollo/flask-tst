from flask import Blueprint, current_app, request
from app.model import Book

from app.serializer import BookSchema

bp_books = Blueprint('books', __name__)

@bp_books.route('/books', methods=['GET'])
def get():
    bs = BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200

@bp_books.route('/books', methods=['POST'])
def post():
    # bs = BookSchema(many=True)
    print(request.json['book'])
    # result = Book.query.all()
    return '---', 200
