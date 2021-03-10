from db import db


class Author(db.Model):
    __tablename__: str = 'books_author'

    id = db.Column(db.Integer, primary_key=True)
    birth_year = db.Column(db.Integer)
    death_year = db.Column(db.Integer)
    name = db.Column(db.String(128))

    @classmethod
    def class_name(cls):
        return 'Author'

    def data_format(self):
        return {
            "birth_year": self.birth_year,
            "death_year": self.death_year,
            "name": self.name
        }
