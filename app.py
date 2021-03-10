import os

import werkzeug
from flask import Flask, jsonify
from flask import request

from db import db
from models.author import Author
from models.book import Book
from models.book_authors import BookAuthors
from models.book_bookshelves import BookShelves
from models.book_languages import BookLanguages
from models.book_subjects import BookSubjects
from models.bookshelf import BookShelf
from models.format import Format
from models.languages import Languages
from models.subject import Subject
from models.util import get_data

app = Flask(__name__)
db.init_app(app)
app.config['SECRET_KEY'] = os.urandom(12).hex()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return jsonify({"message": 'Bad Request!', "code": 400})


@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_bad_request(e):
    return jsonify({"message": 'Not Found!', "code": 404})


@app.errorhandler(werkzeug.exceptions.InternalServerError)
def handle_bad_request(e):
    return jsonify({"message": 'Internal Server Error!', "code": 500})


@app.route("/")
def index():
    page = request.args.get('page', default=1, type=int)
    page_size = int(os.getenv("PAGE_SIZE", 1))

    book_id = request.args.get('book_id', default=None, type=str)
    language = request.args.get('language', default=None, type=str)
    mime_type = request.args.get('mime-type', default=None, type=str)
    topic = request.args.get('topic', default=None, type=str)
    author = request.args.get('author', default=None, type=str)
    title = request.args.get('title', default=None, type=str)

    data = Book.filter(page, page_size,
                       [int(value.strip()) for value in book_id.split(',')] if book_id else [],
                       [value.strip() for value in language.split(',')] if language else [],
                       [value.strip() for value in mime_type.split(',')] if mime_type else [],
                       [value.strip() for value in topic.split(',')] if topic else [],
                       [value.strip() for value in author.split(',')] if author else [],
                       [value.strip() for value in title.split(',')] if title else [])

    return jsonify({"data": get_data(data.items), "page": page}), 200


# Shell Commands Start
@app.shell_context_processor
def inject_models():
    return {
        'Author': Author,
        'Book': Book,
        'BookAuthors': BookAuthors,
        'BookShelves': BookShelves,
        'BookLanguages': BookLanguages,
        'BookSubjects': BookSubjects,
        'BookShelf': BookShelf,
        'Format': Format,
        'Languages': Languages,
        "Subject": Subject
    }
# Shell Commands End


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)
