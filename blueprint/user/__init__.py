from blueprint import db
from flask_restful import fields

class ListUser(db.Model):

    __tablename__ = "ListUser"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    mode = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))
    

    response_field = {
        'id' : fields.Integer,
        'name' : fields.String,
        'email' : fields.String,
        'phone_number' : fields.String,
        'username' : fields.String,
        'password' : fields.String,
        'mode' : fields.String,
        'created_at' : fields.String,
        'updated_at' : fields.String
        
    }
    def __init__(self, id, name, email, phone_number, username, password, mode, created_at, updated_at):
        
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.mode = mode
        self.created_at = created_at
        self.updated_at = updated_at
        

    def __repr__(self):
        return '<User %r>' % self.id