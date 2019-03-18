import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import jwt_required
from blueprint.user import *
from blueprint.book import *
from . import *

bp_rent = Blueprint('rent', __name__)
api = Api(bp_rent)

class RentResource(Resource):

    def __init__(self):
        pass

    def get(self, rent_id = None):
        if rent_id == None :
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=5)
            args = parser.parse_args()

            offset = (args['p'] * args['rp']) - args['rp']


            qry_all = ListRent.query

            list_get_all = []

            for data in qry_all.limit(args['rp']).offset(offset).all() :
                qry_book = ListBook.query.get(marshal(data, ListRent.response_field)['book_id'])
                qry_user = ListUser.query.get(marshal(data, ListRent.response_field)['user_id'])

                datas = marshal(data, ListRent.response_field)
                datas['user'] = marshal(qry_user, ListUser.response_field)
                datas['book'] = marshal(qry_book, ListBook.response_field)
                list_get_all.append(datas)
            return list_get_all, 200, {'Content-Type':'application/json'}

        else :
            qry_id = ListRent.query.get(rent_id)
            if qry_id != None :

                qry_book = ListBook.query.get(marshal(qry_id, ListRent.response_field)['book_id'])
                qry_user = ListUser.query.get(marshal(qry_id, ListRent.response_field)['user_id'])

                datas = marshal(qry_id, ListRent.response_field)
                datas['user'] = marshal(qry_user, ListUser.response_field)
                datas['book'] = marshal(qry_book, ListBook.response_field)

                return datas, 200, {'Content-Type':'application/json'}
            return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('book_id', location='json')
        parser.add_argument('user_id', location='json')
        args = parser.parse_args()
        qry_book = ListBook.query.get(args['book_id'])
        qry_user = ListUser.query.get(args['user_id'])

        list_rent = ListRent(None, args['book_id'], args['user_id'])
        db.session.add(list_rent)
        db.session.commit()

        return marshal(list_rent, ListRent.response_field), 200, {'Content-Type':'application/json'}
    
api.add_resource(RentResource, '/rent', '/rent/<int:rent_id>')