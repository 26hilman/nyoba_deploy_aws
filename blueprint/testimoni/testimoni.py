import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
import datetime
from . import *

bp_testimoni = Blueprint('testimoni', __name__)
api = Api(bp_testimoni)

class TestimoniResource(Resource):

    def __init__(self):
        pass

    @jwt_required
    def get(self, id = None):
        if id == None :
            if(get_jwt_claims()['mode'] == "admin"):
                parser = reqparse.RequestParser()
                parser.add_argument('p', type=int, location='args', default=1)
                parser.add_argument('rp', type=int, location='args', default=999)
                args = parser.parse_args()

                offset = (args['p'] * args['rp']) - args['rp']

                qry_all = ListTestimoni.query

                list_get_all = []

                for data in qry_all.limit(args['rp']).offset(offset).all() :
                    list_get_all.append(marshal(data, ListTestimoni.response_field))
                return {"Status" : "Completed", "Data" : list_get_all}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message" : "Only admin is allowed"},404, {'Content-Type':'application/json'}

        else :
            if(get_jwt_claims()['mode'] == "admin"):
                qry_id = ListTestimoni.query.get(id)
                if qry_id != None :
                    return {"Status" : "Completed", "Data" : marshal(qry_id, ListTestimoni.response_field)}, 200, {'Content-Type':'application/json'}
                return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message" : "Only admin is allowed"}, 404, {'Content-Type':'application/json'}
        
    @jwt_required   
    def delete(self, id):
        if(get_jwt_claims()['mode'] == "admin") :
            qry_delete = ListTestimoni.query.get(id)
            if qry_delete != None :
                db.session.delete(qry_delete)
                db.session.commit()
                return {"Status" : "Complete", "Message" :"Delete Completed"}, 200, {'Content-Type':'application/json'}
            return {"Status": 'Uncompleted', "Message" : "Data Not Found"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message" : "Only Admin Allowed"}, 404, {'Content-Type':'application/json'}
    
  
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('testimoni', location='json', required=True)
        args = parser.parse_args()
        
        user_id = (get_jwt_claims()['id'])
        posted_by = (get_jwt_claims()['name'])
        created_at = datetime.datetime.now().strftime("%c")

        list_testimoni = ListTestimoni(None, user_id, posted_by, args['testimoni'],  "tidak_ditampilkan", created_at, None)
        db.session.add(list_testimoni)
        db.session.commit()

        return { "Status" : "Completed", "Data" : marshal(list_testimoni, ListTestimoni.response_field)}, 200, {'Content-Type':'application/json'}

    @jwt_required
    def put(self, id):
        if get_jwt_claims()['mode'] == 'admin' :
            parser = reqparse.RequestParser()
            parser.add_argument('status', location='json')
            args = parser.parse_args()

            qry_put = ListTestimoni.query.get(id)
            if qry_put != None :
                qry_put.status = args['status']
                qry_put.updated_at = datetime.datetime.now().strftime("%c")
                db.session.commit()
                return {"Status" : "Completed", "Data" : marshal(qry_put, ListMobil.response_field)}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message" : "Only admin is allowed"}, 404, {'Content-Type':'application/json'}
        
api.add_resource(TestimoniResource, '/testimoni', '/testimoni/<int:id>')