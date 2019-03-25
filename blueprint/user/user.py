import logging, json
from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from blueprint import db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
import datetime
from . import *

bp_user = Blueprint('user', __name__)
api = Api(bp_user)

class UserResource(Resource):

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

                qry_all = ListUser.query

                list_get_all = []

                for data in qry_all.limit(args['rp']).offset(offset).all() :
                    list_get_all.append(marshal(data, ListUser.response_field))
                return {"Status" : "Completed", "Data" : list_get_all}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message" : "Only admin is allowed"},404, {'Content-Type':'application/json'}

        else :
            qry_id = ListUser.query.get(id)
            if qry_id != None :
                return {"Status" : "Completed", "Data" : marshal(qry_id, ListUser.response_field)}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message": "Data Not Match"}, 404, {'Content-Type':'application/json'}
    
    @jwt_required
    def put(self, id):
        if(get_jwt_claims()['mode'] == "admin") or (get_jwt_claims()['id'] == id):
            parser = reqparse.RequestParser()
            parser.add_argument('name', location='json')
            parser.add_argument('email', location='json')
            parser.add_argument('phone_number', location='json')
            parser.add_argument('username', location='json')
            parser.add_argument('password', location='json')
            args = parser.parse_args()

            qry_put = ListUser.query.get(id)
            if qry_put != None :
                qry_put.name = args['name']
                qry_put.email = args['email']
                qry_put.phone_number = args['phone_number']
                qry_put.username = args['username']
                qry_put.password = args['password']
                qry_put.updated_at = datetime.datetime.now().strftime("%c")
                db.session.commit()
                return {"Status" : "Completed", "Message" : marshal(qry_put, ListUser.response_field)}, 200, {'Content-Type':'application/json'}
            return {"Status" : "Uncompleted", "Message": "Data Not Found"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message": "Authentication Failed"}, 404, {'Content-Type':'application/json'}
        

    @jwt_required   
    def delete(self, id):
        if(get_jwt_claims()['mode'] == "admin") or (get_jwt_claims()['id'] == id) :
            qry_delete = ListUser.query.get(id)
            if qry_delete != None :
                db.session.delete(qry_delete)
                db.session.commit()
                return {"Status" : "Complete", "Message" :"Delete Completed"}, 200, {'Content-Type':'application/json'}
            return {"Status": 'Uncompleted', "Message" : "Data Not Found"}, 404, {'Content-Type':'application/json'}
        return {"Status" : "Uncompleted", "Message" : "Authentication Failed"}, 404, {'Content-Type':'application/json'}
    
  
    @jwt_required
    def post(self):
        if(get_jwt_claims()['mode'] != "admin"):
            return {"Status" : "Uncompleted", "Message" : "Only admin is allowed"},404, {'Content-Type':'application/json'}
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('phone_number', location='json', required=True)
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('mode', location='json', required=True)
        args = parser.parse_args()
        
        created_at = datetime.datetime.now().strftime("%c")

        list_user = ListUser(None, args['name'], args['email'], args['phone_number'], args['username'], args['password'], args['mode'], created_at, None)
        db.session.add(list_user)
        db.session.commit()
        

        return { "Status" : "Completed", "Data" : marshal(list_user, ListUser.response_field)}, 200, {'Content-Type':'application/json'}

class UserRegisterResource(Resource):

    def __init__(self):
        pass
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('phone_number', location='json', required=True)
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        args = parser.parse_args()
        
        created_at = datetime.datetime.now().strftime("%c")

        list_user_reg = ListUser(None, args['name'], args['email'], args['phone_number'], args['username'], args['password'], "pelapak", created_at, None)
        db.session.add(list_user_reg)
        db.session.commit()

        return {"Status" : "Completed", "Message" : "Regiter Success"}, 200, {'Content-Type':'application/json'}

class UserLoginResource(Resource):

    def __init__(self):
        pass
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        args = parser.parse_args()
        
        qry = ListUser.query.filter_by(username=args['username']).filter_by(password=args['password']).first()
        if qry != None :
            token = create_access_token(marshal(qry, ListUser.response_field))
        else : 
            return {"Status" : "Uncompleted", "Message" : "Invalid Username or Password"}, 401, {'Content-Type':'application/json'}
        return {"Status" : "Completed", "Token" : token}, 200, {'Content-Type':'application/json'}


api.add_resource(UserResource, '/user', '/user/<int:id>')
api.add_resource(UserRegisterResource, '/user/register')
api.add_resource(UserLoginResource, '/user/login')