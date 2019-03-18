import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import jwt_required

from . import *

bp_buku = Blueprint('book', __name__)
api = Api(bp_buku)

class BookResource(Resource):

    def __init__(self):
        pass

    def get(self, book_id = None):
        if book_id == None :
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=5)
            parser.add_argument('title', location='args')
            parser.add_argument('isbn', type=int, location='args')
            args = parser.parse_args()


            offset = (args['p'] * args['rp']) - args['rp']

            qry_all = ListBook.query

            if args['title'] != None:
                qry_all = qry_all.filter(ListBook.name.like("%"+args['title']+"%"))
            elif args['isbn'] != None:
                qry_all = qry_all.filter(ListBook.name.like("%"+args['isbn']+"%"))

            list_get_all = []

            for data in qry_all.limit(args['rp']).offset(offset).all() :
                list_get_all.append(marshal(data, ListBook.response_field))
            return list_get_all, 200, {'Content-Type':'application/json'}

        else :
            qry_id = ListBook.query.get(book_id)
            if qry_id != None :
                return marshal(qry_id, ListBook.response_field), 200, {'Content-Type':'application/json'}
            return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def put(self, book_id):
        parser = reqparse.RequestParser()
        parser.add_argument('id', location='json', type=int, required=True)
        parser.add_argument('title', location='json')
        parser.add_argument('isbn', location='json')
        parser.add_argument('writer', location='json')
        args = parser.parse_args()

        qry_put = ListBook.query.get(book_id)
        if qry_put != None :
            qry_put.id = args['id']
            qry_put.title = args['title']
            qry_put.isbn = args['isbn']
            qry_put.writer = args['writer']
            db.session.commit()
            return marshal(qry_put, ListBook.response_field), 200, {'Content-Type':'application/json'}
        return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}

    @jwt_required    
    def delete(self, book_id):
        qry_delete = ListBook.query.get(book_id)
        if qry_delete != None :
            db.session.delete(qry_delete)
            db.session.commit()
            return 'Delete Completed', 200, {'Content-Type':'application/json'}
        return {'status': 'NOT_FOUND'}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', location='json')
        parser.add_argument('isbn', location='json')
        parser.add_argument('writer', location='json')
        args = parser.parse_args()

        list_book = ListBook(None, args['title'], args['isbn'], args['writer'])
        db.session.add(list_book)
        db.session.commit()

        return marshal(list_book, ListBook.response_field), 200, {'Content-Type':'application/json'}
    
api.add_resource(BookResource, '/book', '/book/<int:book_id>')