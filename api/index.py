from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jokes.db'
db = SQLAlchemy(app)


class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Jokes API',
                    'endpoints': ['/random', '/get', '/add']}), 200

@app.route('/all', methods=['GET'])
def all_jokes():
    jokes = Joke.query.all()
    if jokes:
        return jsonify({'jokes': [joke.content for joke in jokes],
                        'ids': [joke.id for joke in jokes]})
    else:
        return jsonify({'message': 'No jokes found'}), 404

@app.route('/random', methods=['GET'])
def random_joke():
    jokes = Joke.query.all()
    if jokes:
        joke = random.choice(jokes)
        return jsonify({'joke': joke.content,
                        "id": joke.id})
    else:
        return jsonify({'message': 'No jokes found'}), 404

@app.route('/get', methods=['GET'])
def get_joke():
    data = request.get_json()
    name = request.args.get('id')
    joke = Joke.query.filter_by(id=name).first()
    if joke:
        return jsonify({'joke': joke.content})
    else:
        return jsonify({'message': 'No jokes found'}), 404

@app.route('/add', methods=['POST'])
def add_joke():
    data = request.get_json()
    app.logger.info(f"Received data: {data}")
    if not data or 'content' not in data:
        app.logger.error("Invalid request: No data or 'content' field missing")
        return jsonify({'message': 'Invalid request'}), 400
    try:
        new_joke = Joke(content=data['content'])
        db.session.add(new_joke)
        db.session.commit()
        app.logger.info(f"Joke added successfully with ID: {new_joke.id}")
        return jsonify({'message': 'Joke added successfully', 'id': new_joke.id}), 201
    except Exception as e:
        app.logger.error(f"Error adding joke: {e}")
        return jsonify({'message': 'Internal Server Error', 'error': str(e)}), 500

@app.route('/delete_db', methods=['GET'])
def delete_db():
    db.drop_all()

    db.create_all()
    return jsonify({'message': 'Database deleted successfully'}), 200

@app.route('/delete', methods=['DELETE'])
def delete_joke():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({'message': 'Invalid request'}), 400
    joke = Joke.query.filter_by(id=data['id']).first()
    if joke:
        db.session.delete(joke)
        db.session.commit()
        return jsonify({'message': 'Joke deleted successfully'}), 200
    else:
        return jsonify({'message': 'No jokes found'}), 404

if __name__ == '__main__':
    app.run(debug=True)