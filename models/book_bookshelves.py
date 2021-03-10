from db import db
from sqlalchemy.orm import relationship


class BookShelves(db.Model):
    __tablename__: str = 'books_book_bookshelves'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'))
    bookshelf_id = db.Column(db.Integer, db.ForeignKey('books_bookshelf.id'))

    book = relationship("Book", foreign_keys=book_id, backref='bookshelf_books')
    bookshelf = relationship("BookShelf", foreign_keys=bookshelf_id, backref='bookshelves')

    @classmethod
    def class_name(cls):
        return 'BookShelves'

    def data_format(self):
        return {
            "book_id": self.book_id,
            "bookshelf_id": self.bookshelf_id
        }
