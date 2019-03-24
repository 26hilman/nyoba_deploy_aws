import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import jwt_required, get_jwt_claims
import datetime

from . import *

bp_forum = Blueprint('forum', __name__)
api = Api(bp_forum)

class ForumResource(Resource):

    def __init__(self):
        pass

    def get(self, id = None):
        if id == None :
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=999)
            args = parser.parse_args()

            offset = (args['p'] * args['rp']) - args['rp']

            qry_all = ListForum.query

            list_get_all = []

            for data in qry_all.limit(args['rp']).offset(offset).all() :
                list_get_all.append(marshal(data, ListForum.response_field))
            return {"Status" : "Completed", "Data" : list_get_all}, 200, {'Content-Type':'application/json'}

        else :
            qry_id = ListForum.query.get(id)
            if qry_id != None :
                return {"Status" : "Completed", "Data" : marshal(qry_id, ListForum.response_field)}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('judul_post', location='json')
        parser.add_argument('isi_post', location='json')
        args = parser.parse_args()

        qry_put = ListForum.query.get(id)
        if qry_put != None :
            if get_jwt_claims()['mode'] == 'admin' or get_jwt_claims()['id'] == marshal(qry_put, ListForum.response_field)['user_id']:
                qry_put.judul_post = args['judul_post']
                qry_put.isi_post = args['isi_post']
                qry_put.updated_at = datetime.datetime.now().strftime("%c")
                db.session.commit()
                return {"Status" : "Completed", "Data" : marshal(qry_put, ListForum.response_field)}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "No Permission"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}

    @jwt_required    
    def delete(self, id):
        qry_delete = ListForum.query.get(id)
        if qry_delete != None :
            if get_jwt_claims()['id'] == marshal(qry_delete, ListForum.response_field)['user_id'] or get_jwt_claims()['mode'] == 'admin':
                db.session.delete(qry_delete)
                db.session.commit()
                return {"Status" : "Completed", "Message": "Delete Completed"}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Invalid Token"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
        
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('judul_post', location='json')
        parser.add_argument('isi_post', location='json')
        args = parser.parse_args()

        user_id = (get_jwt_claims()['id'])
        posted_by = (get_jwt_claims()['name'])
        created_at = datetime.datetime.now().strftime("%c")

        list_forum = ListForum(None, user_id, posted_by, args['judul_post'], args['isi_post'], created_at, None)
        db.session.add(list_forum)
        db.session.commit()

        return {"Status" : "Completed", "Data" : marshal(list_forum, ListForum.response_field)}, 200, {'Content-Type':'application/json'}
    
api.add_resource(ForumResource, '/forum', '/forum/<int:id>')