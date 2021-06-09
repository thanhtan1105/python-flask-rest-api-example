from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from product_controller import api as pc
from variants_controller import api as vc
from image_controller import api as ic
from flask_restx import Api

from models import db


app = Flask(__name__)
api = Api(app,
          title='Demo Rest API',
          version='1.0'
          )
api.add_namespace(pc, path='/product')
api.add_namespace(vc, path='/variant')
api.add_namespace(ic, path='/image')

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://tanlt:Br9Oh3Tc2Dg7Xp5C@45.119.82.118:3306/tanlt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy()
db.init_app(app)
app.run(debug=True, host='0.0.0.0')

