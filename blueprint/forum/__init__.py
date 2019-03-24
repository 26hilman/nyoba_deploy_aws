from blueprint import db
from flask_restful import fields
from blueprint.user import __init__

class ListForum(db.Model):

    __tablename__ = "ListForum"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    posted_by = db.Column(db.String(255))
    judul_post = db.Column(db.String(255))
    isi_post = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255)) 

    response_field = {
        'id' : fields.Integer,
        'user_id' : fields.Integer,
        'posted_by' : fields.String,
        'judul_post' : fields.String,
        'isi_post' : fields.String,
        'created_at' : fields.String,
        'updated_at' : fields.String
    }
    def __init__(self, id, user_id, posted_by, judul_post, isi_post, created_at, updated_at):
        
        self.id = id
        self.user_id = user_id
        self.posted_by = posted_by
        self.judul_post = judul_post
        self.isi_post = isi_post
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Forum %r>' % self.id