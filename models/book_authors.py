from db import db
from sqlalchemy.orm import relationship


class BookAuthors(db.Model):
    __tablename__: str = 'books_book_authors'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('books_author.id'))

    book = relationship("Book", foreign_keys=book_id, backref='author_books')
    author = relationship("Author", foreign_keys=author_id, backref='authors')

    @classmethod
    def class_name(cls):
        return 'BookAuthors'

    def data_format(self):
        return {
            "book_id": self.book_id,
            "author_id": self.author_id
        }
