from flask import Flask, jsonify, request

# 
app = Flask(__name__)

notes = [] #data sementara
pesan = [
    {
        "title": "",
        "content": ""             
    }
]

@app.route('/')
def index():
    return jsonify({
        "message": "Selamat datang di Simple Notes API!"
    })

# 
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/notes', methods=['POST'])
def add_notes():
    data = request.json
    notes.append(data)
    return jsonify({"message": "Note added!", "note": data}), 201


@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_route(note_id):
    if note_id >= len(notes):
        return jsonify({"error": "Note not found"}), 404
    data = request.json 
    notes[note_id].update(data)
    return jsonify({"message": "Note updated", "Note": notes[note_id]})

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    if note_id >= len(notes):
        return jsonify({"error": "Note not found"}), 404
    deleted = notes.pop(note_id)
    return jsonify({"message": "Note deleted", "note": deleted})

# Route Pesan
@app.route('/pesan', methods=['GET'])
def get_pesan():
    return jsonify(pesan)

@app.route('/pesan', methods=['POST'])
def add_pesan():
    data = request.json
    pesan.append(data)
    return jsonify({"message": "Pesan added!", "pesan": data}), 201

@app.route('/pesan/<int:pesan_id>', methods=['PUT'])
def update_pesan(pesan_id):
    if pesan_id >= len(pesan):
        return jsonify({"error": "Pesan not found"}), 404
    data = request.json
    pesan[pesan_id].update(data)
    return jsonify({"message": "Pesan updated", "Pesan": pesan[pesan_id]})

@app.route('/pesan/<int:pesan_id>', methods=['DELETE'])
def delete_pesan(pesan_id):
    if pesan_id >= len(pesan):
        return jsonify({"error": "Pesan not found"}), 404
    deleted = pesan.pop(pesan_id)
    return jsonify({"message": "Pesan deleted", "Pesan": deleted})


if __name__ == '__main__':
    app.run(debug=True)