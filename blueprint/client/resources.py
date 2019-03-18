import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import jwt_required

from . import *

bp_client = Blueprint('client', __name__)
api = Api(bp_client)

class ClientResource(Resource):

    def __init__(self):
        pass

    def get(self, client_id = None):
        if client_id == None :
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=5)
            parser.add_argument('id', type=int, location='args')
            parser.add_argument('status', location='args')
            args = parser.parse_args()
            
            offset = (args['p'] * args['rp']) - args['rp']

            qry_all = ListClient.query

            if args['id'] != None:
                qry_all = qry_all.filter(ListClient.name.like("%"+args['id']+"%"))
            elif args['status'] != None:
                qry_all = qry_all.filter(ListClient.name.like("%"+args['status']+"%"))

            list_get_all = []

            for data in qry_all.limit(args['rp']).offset(offset).all() :
                list_get_all.append(marshal(data, ListClient.response_field))
            return list_get_all, 200, {'Content-Type':'application/json'}

        else :
            qry_id = ListClient.query.get(client_id)
            if qry_id != None :
                return marshal(qry_id, ListClient.response_field), 200, {'Content-Type':'application/json'}
            return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def put(self, client_id):
        parser = reqparse.RequestParser()
        parser.add_argument('id', location='json', type=int, required=True)
        parser.add_argument('client_key', location='json')
        parser.add_argument('client_secret', location='json')
        parser.add_argument('status', location='json')
        args = parser.parse_args()

        qry_put = ListClient.query.get(client_id)
        if qry_put != None :
            qry_put.id = args['id']
            qry_put.client_key = args['client_key']
            qry_put.client_secret = args['client_secret']
            qry_put.status = args['status']
            db.session.commit()
            return marshal(qry_put, ListClient.response_field), 200, {'Content-Type':'application/json'}
        return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}

    @jwt_required   
    def delete(self, client_id):
        qry_delete = ListClient.query.get(client_id)
        if qry_delete != None :
            db.session.delete(qry_delete)
            db.session.commit()
            return 'Delete Completed', 200, {'Content-Type':'application/json'}
        return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location='json')
        parser.add_argument('client_secret', location='json')
        parser.add_argument('status', type=bool, location='json')
        args = parser.parse_args()
        print(args)
        
        list_client = ListClient(None, args['client_key'], args['client_secret'], args['status'])
        db.session.add(list_client)
        db.session.commit()

        return marshal(list_client, ListClient.response_field), 200, {'Content-Type':'application/json'}
    
api.add_resource(ClientResource, '/client', '/client/<int:client_id>')