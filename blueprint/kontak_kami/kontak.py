import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import jwt_required, get_jwt_claims
import datetime
from . import *

bp_kontakkami = Blueprint('kontakkami', __name__)
api = Api(bp_kontakkami)

class TestimoniResource(Resource):

    def __init__(self):
        pass

    @jwt_required
    def get(self, id = None):
        if get_jwt_claims()['mode'] == 'admin' :
            if id == None :
                parser = reqparse.RequestParser()
                parser.add_argument('p', type=int, location='args', default=1)
                parser.add_argument('rp', type=int, location='args', default=999)
                args = parser.parse_args()
                offset = (args['p'] * args['rp']) - args['rp']
                qry_all = ListKontakKami.query
                list_get_all = []
                for data in qry_all.limit(args['rp']).offset(offset).all() :
                    list_get_all.append(marshal(data, ListKontakKami.response_field))
                return {"Status" : "Completed", "Data" : list_get_all}, 200, {'Content-Type':'application/json'}

            else :
                qry_id = ListKontakKami.query.get(id)
                if qry_id != None :
                    return {"Status" : "Completed", "Data" : marshal(qry_id, ListKontakKami.response_field)}, 200, {'Content-Type':'application/json'}
                return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Data Not Match"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message": "Only Admin Allowed"}, 404, {'Content-Type':'application/json'}
            
    
  
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('nomor_telepon', location='json', required=True)
        parser.add_argument('pesan', location='json', required=True)
        args = parser.parse_args()
        
        created_at = datetime.datetime.now().strftime("%c")

        list_kontakkami = ListKontakKami(None, args['nama'], args['email'], args['nomor_telepon'], args['pesan'], created_at)
        db.session.add(list_kontakkami)
        db.session.commit()

        return { "Status" : "Completed", "Data" : marshal(list_kontakkami, ListKontakKami.response_field)}, 200, {'Content-Type':'application/json'}
        
api.add_resource(TestimoniResource, '/kontakkami', '/kontakkami/<int:id>')