from blueprint import db
from flask_restful import fields

class ListUser(db.Model):

    __tablename__ = "ListUser"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    sex = db.Column(db.String(10))
    client_id = db.Column(db.Integer)

    response_field = {
        'id' : fields.Integer,
        'name' : fields.String,
        'age' : fields.Integer,
        'sex' : fields.String,
        'client_id' : fields.Integer
    }

    def __init__(self, id, name, age, sex, client_id):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.client_id = client_id

    def __repr__(self):
        return '<User %r>' % self.id
