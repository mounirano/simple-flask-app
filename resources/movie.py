from flask_restful import Resource

from shared import create_parser
from models.movie import MovieModel


class Movie(Resource):

    post_parser_args = [
        {'name': 'name', 'type': str, 'required': True},
        {'name': 'genre', 'type': str, 'required': True},
        {'name': 'rel_date', 'type': str, 'required': True},
        {'name': 'added_by', 'type': str, 'required': True}
    ]

    get_parser_args = [
        {'name': 'name', 'type': str, 'required': True}
    ]

    def post(self, **kwargs):
        post_parser = create_parser(self.post_parser_args)
        request_data = post_parser.parse_args()

        movie_exist = MovieModel.query.filter_by(name=request_data['name']).first()

        if movie_exist:
            return {'error': 'Movie already exists'}, 409

        add_new_movie = MovieModel(**request_data)
        try:
            add_new_movie.save_to_db()
        except:
            return {'error': "something went wrong"}, 500
        return add_new_movie.json(), 201

    def get(self, **kwargs):
        get_parser = create_parser(self.get_parser_args)
        request_data = get_parser.parse_args()

        movie = MovieModel.query.filter_by(name=request_data['name']).first()

        if not movie:
            return {'error': 'Movie not found'}, 404

        return [
            movie.json() for movie in MovieModel.query
            .filter_by(name=request_data['name'])
            .all()
        ]
