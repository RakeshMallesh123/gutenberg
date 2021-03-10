from db import db


class BookShelf(db.Model):
    __tablename__: str = 'books_bookshelf'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    @classmethod
    def class_name(cls):
        return 'BookShelf'

    def data_format(self):
        return {
            "name": self.name
        }
