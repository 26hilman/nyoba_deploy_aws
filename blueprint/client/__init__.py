from blueprint import db
from flask_restful import fields

class ListClient(db.Model):

    __tablename__ = "ListClient"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    client_key = db.Column(db.String(255))
    client_secret = db.Column(db.String(255))
    status = db.Column(db.Boolean)

    response_field = {
        'id' : fields.Integer,
        'client_key' : fields.String,
        'client_secret' : fields.String,
        'status' : fields.Boolean
    }
    def __init__(self, id, client_key, client_secret, status):
        print(client_key)
        self.id = id
        self.client_key = client_key
        self.client_secret = client_secret
        self.status = status

    def __repr__(self):
        return '<Client %r>' % self.id