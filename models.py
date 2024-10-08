from flask_sqlalchemy import SQLAlchemy
from serializers import SerializerMixin

db = SQLAlchemy()

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movie'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    movie_image = db.Column(db.Text)
    genre = db.Column(db.Text)
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'), nullable=False)
    
    def movie_serializer(self):
        return {
            'id': self.id,
            'title': self.title,
            'movie_image': self.movie_image,
            'genre': self.genre
        }



class Actor(db.Model, SerializerMixin):
    __tablename__ = 'actor'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String)
    movies = db.relationship('Movie', backref='actor')
    
    def actor_serializer(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            # Serialize movies using their own serializer
            'movies': [movie.movie_serializer() for movie in self.movies]
        }

