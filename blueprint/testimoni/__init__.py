from blueprint import db
from flask_restful import fields

class ListTestimoni(db.Model):

    __tablename__ = "ListTestimoni"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    posted_by = db.Column(db.String(255))
    testimoni = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255))
    

    response_field = {
        'id' : fields.Integer,
        'user_id' : fields.String,
        'posted_by' : fields.String,
        'testimoni' : fields.String,
        'status' : fields.String,
        'created_at' : fields.String,
        'updated_at' : fields.String
        
    }
    def __init__(self, id, user_id, posted_by, testimoni, status, created_at, updated_at):
        
        self.id = id
        self.user_id = user_id
        self.posted_by = posted_by
        self.testimoni = testimoni
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        

    def __repr__(self):
        return '<Testimoni %r>' % self.id