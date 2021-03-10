from db import db
from sqlalchemy.orm import relationship


class BookLanguages(db.Model):
    __tablename__: str = 'books_book_languages'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('books_language.id'))

    book = relationship("Book", foreign_keys=book_id, backref='language_books')
    language = relationship("Languages", foreign_keys=language_id, backref='languages')

    @classmethod
    def class_name(cls):
        return 'BookLanguages'

    def data_format(self):
        return {
            "book_id": self.book_id,
            "language_id": self.language_id
        }
