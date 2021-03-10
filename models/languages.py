from db import db


class Languages(db.Model):
    __tablename__: str = 'books_language'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4))

    @classmethod
    def class_name(cls):
        return 'Languages'

    def data_format(self):
        return {
            "code": self.code
        }
