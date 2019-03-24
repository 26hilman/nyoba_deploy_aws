import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import jwt_required, get_jwt_claims
import datetime

from . import *

bp_mobil = Blueprint('mobil', __name__)
api = Api(bp_mobil)

class MobilResource(Resource):

    def __init__(self):
        pass

    def get(self, id = None):
        if id == None :
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=5)
            args = parser.parse_args()

            offset = (args['p'] * args['rp']) - args['rp']

            qry_all = ListMobil.query

            list_get_all = []

            for data in qry_all.limit(args['rp']).offset(offset).all() :
                list_get_all.append(marshal(data, ListMobil.response_field))
            return {"Status" : "Completed", "Data" : list_get_all}, 200, {'Content-Type':'application/json'}

        else :
            qry_id = ListMobil.query.get(id)
            if qry_id != None :
                return {"Status" : "Completed", "Data" : marshal(qry_id, ListMobil.response_field)}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('merk_mobil', location='json')
        parser.add_argument('model_mobil', location='json')
        parser.add_argument('transmisi', location='json')
        parser.add_argument('jarak_tempuh', location='json')
        parser.add_argument('tahun', location='json')
        parser.add_argument('tipe_bahan_bakar', location='json')
        parser.add_argument('warna_mobil', location='json')
        parser.add_argument('harga', location='json')
        parser.add_argument('judul_lapak', location='json')
        parser.add_argument('deskripsi_lapak', location='json')
        parser.add_argument('url_gambar', location='json')
        args = parser.parse_args()

        qry_put = ListMobil.query.get(id)
        if qry_put != None :
            if get_jwt_claims()['mode'] == 'admin' or get_jwt_claims()['id'] == marshal(qry_put, ListMobil.response_field)['user_id']:
                qry_put.merk_mobil = args['merk_mobil']
                qry_put.model_mobil = args['model_mobil']
                qry_put.transmisi = args['transmisi']
                qry_put.jarak_tempuh = args['jarak_tempuh']
                qry_put.tahun = args['tahun']
                qry_put.tipe_bahan_bakar = args['tipe_bahan_bakar']
                qry_put.warna_mobil = args['warna_mobil']
                qry_put.harga = args['harga']
                qry_put.judul_lapak = args['judul_lapak']
                qry_put.deskripsi_lapak = args['deskripsi_lapak']
                qry_put.url_gambar = args['url_gambar']
                qry_put.updated_at = datetime.datetime.now().strftime("%c")
                db.session.commit()
                return {"Status" : "Completed", "Data" : marshal(qry_put, ListMobil.response_field)}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "No Permission"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}

    @jwt_required    
    def delete(self, id):
        qry_delete = ListMobil.query.get(id)
        if qry_delete != None :
            if get_jwt_claims()['id'] == marshal(qry_delete, ListMobil.response_field)['user_id'] or get_jwt_claims()['mode'] == 'admin':
                db.session.delete(qry_delete)
                db.session.commit()
                return {"Status" : "Completed", "Message": "Delete Completed"}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Invalid Token"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
        
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('merk_mobil', location='json')
        parser.add_argument('model_mobil', location='json')
        parser.add_argument('transmisi', location='json')
        parser.add_argument('jarak_tempuh', location='json')
        parser.add_argument('tahun', location='json')
        parser.add_argument('tipe_bahan_bakar', location='json')
        parser.add_argument('warna_mobil', location='json')
        parser.add_argument('harga', location='json')
        parser.add_argument('judul_lapak', location='json')
        parser.add_argument('deskripsi_lapak', location='json')
        parser.add_argument('url_gambar', location='json')
        args = parser.parse_args()

        user_id = (get_jwt_claims()['id'])
        posted_by = (get_jwt_claims()['name'])
        created_at = datetime.datetime.now().strftime("%c")

        list_mobil = ListMobil(None, user_id, posted_by, args['merk_mobil'], args['model_mobil'], args['transmisi'], args['jarak_tempuh'], args['tahun'], args['tipe_bahan_bakar'], args['warna_mobil'], args['harga'], args['judul_lapak'], args['deskripsi_lapak'], args['url_gambar'], created_at, None)
        db.session.add(list_mobil)
        db.session.commit()

        return {"Status" : "Completed", "Data" : marshal(list_mobil, ListMobil.response_field)}, 200, {'Content-Type':'application/json'}
    
api.add_resource(MobilResource, '/mobil', '/mobil/<int:id>')