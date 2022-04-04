from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask import render_template, request, redirect, json, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3309/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from models.Task import Task



db.create_all()

from schemas.TaskSchema import TaskSchema


# routing 
import routes


if __name__ == '__main__':
    app.run(debug=True)
