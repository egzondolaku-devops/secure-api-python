from flask import Blueprint, request, jsonify

routes = Blueprint("routes", __name__)

notes = []  # In-memory lagring av anteckningar

@routes.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()

    if not data or not data.get("title") or not data.get("content"):
        return jsonify({"error": "Invalid input"}), 400

    # Enkel XSS-skydd
    if "<script>" in data["title"].lower() or "<script>" in data["content"].lower():
        return jsonify({"error": "Potential XSS detected"}), 400

    note = {
        "id": len(notes) + 1,
        "title": data["title"],
        "content": data["content"]
    }
    notes.append(note)
    return jsonify(note), 201

@routes.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes), 200

@routes.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = next((note for note in notes if note["id"] == note_id), None)
    
    if not note:
        return jsonify({"error": "Note not found"}), 404

    notes.remove(note)
    return jsonify({"message": f"Note {note_id} deleted"}), 200
