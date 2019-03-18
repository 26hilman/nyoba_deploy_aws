import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import jwt_required

from . import *

bp_user = Blueprint('user', __name__)
api = Api(bp_user)



class UserResource(Resource):

    def __init__(self):
        pass

    def get(self, user_id = None):
        if user_id == None :
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=5)
            parser.add_argument('name', location='args')
            args = parser.parse_args()

            offset = (args['p'] * args['rp']) - args['rp']

            qry_all = ListUser.query
            # qry_all = ListUser.query.all()

            if args['name'] != None:
                # qry_all = qry_all.filter_by(name=args['name'])
                qry_all = qry_all.filter(ListUser.name.like("%"+args['name']+"%"))

            list_get_all = []

            for data in qry_all.limit(args['rp']).offset(offset).all() :
                list_get_all.append(marshal(data, ListUser.response_field))
            return list_get_all, 200, {'Content-Type':'application/json'}

        else :
            qry_id = ListUser.query.get(user_id)
            if qry_id != None :
                return marshal(qry_id, ListUser.response_field), 200, {'Content-Type':'application/json'}
            return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('id', location='json', type=int, required=True)
        parser.add_argument('name', location='json')
        parser.add_argument('age', location='json')
        parser.add_argument('sex', location='json')
        parser.add_argument('client_id', location='json', type=int)
        args = parser.parse_args()

        qry_put = ListUser.query.get(user_id)
        if qry_put != None :
            qry_put.id = args['id']
            qry_put.name = args['name']
            qry_put.age = args['age']
            qry_put.sex = args['sex']
            qry_put.client_id = args['client_id']
            db.session.commit()
            return marshal(qry_put, ListUser.response_field), 200, {'Content-Type':'application/json'}
        return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
        
    @jwt_required
    def delete(self, user_id):
        qry_delete = ListUser.query.get(user_id)
        if qry_delete != None :
            db.session.delete(qry_delete)
            db.session.commit()
            return 'Delete Completed', 200, {'Content-Type':'application/json'}
        return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json')
        parser.add_argument('age', location='json')
        parser.add_argument('sex', location='json')
        parser.add_argument('client_id', location='json', type=int)
        args = parser.parse_args()

        list_user = ListUser(None, args['name'], args['age'], args['sex'], args['client_id'])
        db.session.add(list_user)
        db.session.commit()

        return marshal(list_user, ListUser.response_field), 200, {'Content-Type':'application/json'}
    
api.add_resource(UserResource, '/user', '/user/<int:user_id>')