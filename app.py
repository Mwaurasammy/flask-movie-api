from flask import Flask, jsonify
from models import db, Actor
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mwaura:4150@localhost/allmovies'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "<h1>HEY</h1>"

@app.route('/all_actors', methods=['GET'])
def get_all_actors():
    actors = Actor.query.all()
    return jsonify([actor.actor_serializer() for actor in actors])

@app.route('/get_actor/<int:actor_id>', methods=['GET'])
def get_actor(actor_id):
    actor = Actor.query.get(actor_id)
    return jsonify(actor.actor_serializer())

if __name__ == "__main__":
    app.run(debug=True, port=5555)
