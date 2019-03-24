from blueprint import db
from flask_restful import fields

class ListKontakKami(db.Model):

    __tablename__ = "ListKontakKami"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    nama = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    nomor_telpon = db.Column(db.String(255), nullable=True)
    pesan = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.String(255))
    

    response_field = {
        'id' : fields.Integer,
        'nama' : fields.String,
        'email' : fields.String,
        'nomor_telpon' : fields.String,
        'pesan' : fields.String,
        'created_at' : fields.String
        
    }
    def __init__(self, id, nama, email, nomor_telpon, pesan, created_at):
        
        self.id = id
        self.nama = nama
        self.email = email
        self.nomor_telpon = nomor_telpon
        self.pesan = pesan
        self.created_at = created_at
        

    def __repr__(self):
        return '<KontakKami %r>' % self.id