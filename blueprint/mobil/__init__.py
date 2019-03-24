from blueprint import db
from flask_restful import fields
from blueprint.user import __init__

class ListMobil(db.Model):

    __tablename__ = "ListMobil"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    posted_by = db.Column(db.String(255))
    merk_mobil = db.Column(db.String(255), nullable=False)
    model_mobil = db.Column(db.String(255), nullable=False)
    transmisi = db.Column(db.String(255), nullable=False)
    jarak_tempuh = db.Column(db.Integer, nullable=False)
    tahun = db.Column(db.Integer, nullable=False)
    tipe_bahan_bakar = db.Column(db.String(255), nullable=False)
    warna_mobil = db.Column(db.String(255), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    judul_lapak = db.Column(db.Text, nullable=True)
    deskripsi_lapak = db.Column(db.Text, nullable=True)
    url_gambar = db.Column(db.String(255))
    created_at = db.Column(db.String(255))
    updated_at = db.Column(db.String(255)) 

    response_field = {
        'id' : fields.Integer,
        'user_id' : fields.Integer,
        'posted_by' : fields.String,
        'merk_mobil' : fields.String,
        'model_mobil' : fields.String,
        'transmisi' : fields.String,
        'jarak_tempuh' : fields.Integer,
        'tahun' : fields.Integer,
        'tipe_bahan_bakar' : fields.String,
        'warna_mobil' : fields.String,
        'harga' : fields.Integer,
        'judul_lapak' : fields.String,
        'deskripsi_lapak' : fields.String,
        'url_gambar' : fields.String,
        'created_at' : fields.String,
        'updated_at' : fields.String
    }
    def __init__(self, id, user_id, posted_by, merk_mobil, model_mobil, transmisi, jarak_tempuh, tahun, tipe_bahan_bakar, warna_mobil, harga, judul_lapak, deskripsi_lapak, url_gambar, created_at, updated_at):
        
        self.id = id
        self.user_id = user_id
        self.posted_by = posted_by
        self.created_at = created_at
        self.updated_at = updated_at
        self.merk_mobil = merk_mobil
        self.model_mobil = model_mobil
        self.transmisi = transmisi
        self.jarak_tempuh = jarak_tempuh
        self.tahun = tahun
        self.tipe_bahan_bakar = tipe_bahan_bakar
        self.warna_mobil = warna_mobil
        self.harga = harga
        self.judul_lapak = judul_lapak
        self.deskripsi_lapak = deskripsi_lapak
        self.url_gambar = url_gambar
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Mobil %r>' % self.id