from db import db


class MovieModel(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    genre = db.Column(db.String(128), nullable=False)
    rel_date = db.Column(db.String(128), nullable=False)
    added_by = db.Column(db.String(128), nullable=False)
    status = db.Column(db.String(25), nullable=False, default='active')

    def __init__(self, name, genre, rel_date, added_by):
        self.name = name
        self.genre = genre
        self.rel_date = rel_date
        self.added_by = added_by

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'rel_date': self.rel_date,
            'added_by': self.added_by,
            'status': self.status,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
