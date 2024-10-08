from models import Movie, Actor, db
from app import app

with app.app_context():
    # Create actors
    actor1 = Actor(name='actor one', location='actor one local')
    actor2 = Actor(name='actor two', location='actor two local')
    
    # Create movies associated with actors
    movie1 = Movie(title='movie one', movie_image='movie one image link', actor=actor1)
    movie2 = Movie(title='movie two', movie_image='movie two image link', actor=actor1)
    movie3 = Movie(title='movie three', movie_image='movie three image link', actor=actor2)
    
    # Add actors and movies to the session
    db.session.add(actor1)
    db.session.add(actor2)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    
    # Commit the session to persist the data
    db.session.commit()
