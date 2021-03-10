from db import db
from sqlalchemy.orm import relationship


class BookSubjects(db.Model):
    __tablename__: str = 'books_book_subjects'

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books_book.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('books_subject.id'))

    book = relationship("Book", foreign_keys=book_id, backref='subject_books')
    subject = relationship("Subject", foreign_keys=subject_id, backref='subjects')

    @classmethod
    def class_name(cls):
        return 'BookSubjects'

    def data_format(self):
        return {
            "book_id": self.book_id,
            "subject_id": self.subject_id
        }
