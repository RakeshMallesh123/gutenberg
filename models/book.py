from sqlalchemy.sql import text

from db import db
from models.author import Author
from models.book_authors import BookAuthors
from models.book_bookshelves import BookShelves
from models.book_languages import BookLanguages
from models.book_subjects import BookSubjects
from models.bookshelf import BookShelf
from models.format import Format
from models.languages import Languages
from models.subject import Subject
from models.util import get_query_condition


class Book(db.Model):
    __tablename__: str = 'books_book'

    id = db.Column(db.Integer, primary_key=True)
    download_count = db.Column(db.Integer)
    gutenberg_id = db.Column(db.Integer)
    media_type = db.Column(db.String(16))
    title = db.Column(db.String())

    @classmethod
    def class_name(cls):
        return 'Book'

    def data_format(self):
        return {
            "gutenberg_id": self.gutenberg_id,
            "media_type": self.media_type,
            "title": self.title
        }

    @classmethod
    def get_condition(cls, data, ):
        pass

    @classmethod
    def filter(cls, page, page_size, book_ids, languages, mime_types, topics, authors, titles):
        data = db.session.query(Book).distinct()
        if authors:
            condition = get_query_condition("books_author.name", authors)
            data = data.join(BookAuthors, Book.id == BookAuthors.book_id) \
                .join(Author, BookAuthors.author_id == Author.id) \
                .filter(
                    text("(" + condition + ")")
                )
        else:
            data = data.join(BookAuthors, Book.id == BookAuthors.book_id, isouter=True)

        if languages:
            data = data.join(BookLanguages, Book.id == BookLanguages.book_id) \
                .join(Languages, BookLanguages.language_id == Languages.id) \
                .filter(Languages.code.in_(languages))
        else:
            data = data.join(BookLanguages, Book.id == BookLanguages.book_id, isouter=True)

        if mime_types:
            data = data.join(Format, Book.id == Format.book_id) \
                .filter(Format.mime_type.in_(mime_types))
        else:
            data = data.join(Format, Book.id == Format.book_id, isouter=True)

        data = data.join(BookShelves, Book.id == BookShelves.book_id, isouter=True) \
            .join(BookSubjects, Book.id == BookSubjects.book_id, isouter=True)

        if topics:
            condition_subject = get_query_condition("books_subject.name", topics)
            condition_bookshelf = get_query_condition("books_bookshelf.name", topics)
            data = data.join(BookShelf, BookShelves.bookshelf_id == BookShelf.id) \
                .join(Subject, BookSubjects.subject_id == Subject.id)
            data = data.filter(
                text("(" + condition_bookshelf + " OR " + condition_subject + ")")
            )
        if titles:
            condition = get_query_condition("books_book.title", titles)
            data = data.filter(
                text("(" + condition + ")")
            )
        if book_ids:
            data = data.filter(Book.gutenberg_id.in_(book_ids))

        data = data.order_by(Book.download_count.desc()).paginate(page, page_size)

        return data
