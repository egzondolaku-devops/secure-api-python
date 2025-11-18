from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "Invalid input"}), 400

    if "<script>" in data["title"].lower() or "<script>" in data["content"].lower():
        return jsonify({"error": "Potential XSS detected"}), 400

    note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"]
    }
    notes.append(note)
    return jsonify(note), 201


@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes), 200


@app.route('/notes/<int:id>', methods=['DELETE'])
def delete_note(id):
    note_to_delete = next((note for note in notes if note['id'] == id), None)

    if note_to_delete is None:
        return jsonify({"error": "Note not found"}), 404

    notes.remove(note_to_delete)
    return jsonify({"message": f"Note {id} deleted"}), 200


@app.route('/')
def home():
    return {"message": "Hello, DevSecOps world!"}


if __name__ == '__main__':
    app.run(debug=True)