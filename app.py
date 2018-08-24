from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class Historian(db.Model):
    __tablename__ = 'historian'
    id = db.Column(db.Integer, primary_key=True)
    historian_id = db.Column(db.String())
    name = db.Column(db.String())
    date_born = db.Column(db.String())
    place_born = db.Column(db.String())
    date_died = db.Column(db.String())
    place_died = db.Column(db.String())
    overview = db.Column(db.String())
    home_country = db.Column(db.String())
    sources = db.Column(db.String())
    bibliography = db.Column(db.String())
    other_names = db.Column(db.String())
    contributor = db.Column(db.String())
    notes = db.Column(db.String())
    gender = db.Column(db.String())
    subject_area = db.Column(db.String())
    path = db.Column(db.String())

manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Historian, methods=['GET'], allow_patch_many=True, results_per_page=100)


if __name__ == "__main__":
	app.run(debug=True)
