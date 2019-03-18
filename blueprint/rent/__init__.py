from blueprint import db
from flask_restful import fields

class ListRent(db.Model):

    __tablename__ = "ListRent"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    book_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    response_field = {
        'id' : fields.Integer,
        'book_id' : fields.Integer,
        'user_id' : fields.Integer
    }

    def __init__(self, id, book_id, user_id):
        self.id = id
        self.book_id = book_id
        self.user_id = user_id
    
    def __repr__(self):
        return '<Rent %r>' % self.id