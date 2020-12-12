from flask import Flask, Blueprint
from flask_restful import Api

from db import db
from conf import Config

from resources.movie import Movie


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

app = Flask(__name__)
app.config.from_object(Config)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Movie, '/movie')

db.init_app(app)

app.register_blueprint(api_bp, url_prefix='/api')
