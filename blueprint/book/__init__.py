from blueprint import db
from flask_restful import fields

class ListBook(db.Model):

    __tablename__ = "ListBook"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    title = db.Column(db.String(255))
    isbn = db.Column(db.String(255))
    writer = db.Column(db.String(255))

    response_field = {
        'id' : fields.Integer,
        'title' : fields.String,
        'isbn' : fields.String,
        'writer' : fields.String
    }

    def __init__(self, id, title, isbn, writer):
        self.id = id
        self.title = title
        self.isbn = isbn
        self.writer = writer
    
    def __repr__(self):
        return '<Book %r>' % self.id