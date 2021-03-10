from db import db
from sqlalchemy.orm import relationship


class Format(db.Model):
    __tablename__: str = 'books_format'

    id = db.Column(db.Integer, primary_key=True)
    mime_type = db.Column(db.String(32))
    url = db.Column(db.String())
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'))

    book = relationship("Book", foreign_keys=book_id, backref='format_books')

    @classmethod
    def class_name(cls):
        return 'Format'

    def data_format(self):
        return {
            "mime_type": self.mime_type,
            "url": self.url
        }
