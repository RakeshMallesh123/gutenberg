from db import db


class Subject(db.Model):
    __tablename__: str = 'books_subject'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    @classmethod
    def class_name(cls):
        return 'Subject'

    def data_format(self):
        return {
            "name": self.name
        }
