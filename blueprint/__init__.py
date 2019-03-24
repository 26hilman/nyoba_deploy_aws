from flask import Flask, request
import json, logging
from flask_restful import Resource, Api, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@api.clclkjmy7ppm.ap-southeast-1.rds.amazonaws.com/Portofolio_API'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'SADASsadsadsadsadSADsafaSAdsa0921'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return identity

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

api = Api(app, catch_all_404s=True)

@app.after_request
def after_request(response):
    if request.method == 'GET':
        app.logger.warning("REQUEST LOG\t%s %s", request.method, json.dumps({'request': request.args.to_dict(), 'response': json.loads(response.data.decode('utf-8'))}))
    else :
        app.logger.warning("REQUEST LOG\t%s %s", request.method, json.dumps({'request': request.get_json(), 'response': json.loads(response.data.decode('utf-8'))}))
    return response

## call blueprint
from blueprint.user.user import bp_user
from blueprint.mobil.mobil import bp_mobil
from blueprint.testimoni.testimoni import bp_testimoni
from blueprint.kontak_kami.kontak import bp_kontakkami
from blueprint.forum.forum import bp_forum

app.register_blueprint(bp_user)
app.register_blueprint(bp_mobil)
app.register_blueprint(bp_testimoni)
app.register_blueprint(bp_kontakkami)
app.register_blueprint(bp_forum)


db.create_all()

