import json
from Flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from Models import Note

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = False

db = SQLAlchemy(app)

from models import Note # IMPORT MODEL SETELAH DB DIBUAT

@app.route('/')
def index():
    return jsonify({"message": "API with Database READY!"})

@app.route('/notes')
def get_notes():
    notes = Note.query.all()
    return jsonify([n.to_dict() for n in notes])

@app.route('/notes', methods=['POST'])
def add_notes():
    data = request.json
    new_note = Note(title=data['title'], content=data['content'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "Note added!", "note": new_note.to_dict()}), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_notes(note_id):
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"error": "Not Found"}), 404
    data = request.json
    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)
    db.session.commit()
    return jsonify({"message": "Update!", "note": note.to_dict()})

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_notes(note_id):
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"error": "Not Found"}), 404
    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Deleted!", "note": note.to_dict()})


if __name__ == '__name__':
    with app.app_context():
        db.create_all() # Buat Table otomatis
    app.run(debug=True)