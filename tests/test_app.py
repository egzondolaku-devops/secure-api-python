import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from app import app

# Skapar en test-klient för att testa API:t
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Testar att man kan hämta alla anteckningar
def test_get_notes(client):
    response = client.get('/notes')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

# Testar att skapa en ny anteckning
def test_create_note(client):
    response = client.post("/notes", json={
        "title": "Testtitel",
        "content": "Detta är ett test"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Testtitel"
    assert data["content"] == "Detta är ett test"
    assert "id" in data  # Säkerställer att ett ID skapas

# Testar att ta bort en anteckning
def test_delete_note(client):
    # Skapar en anteckning först
    response = client.post("/notes", json={
        "title": "Att ta bort",
        "content": "Denna ska tas bort"
    })
    note = response.get_json()
    note_id = note["id"]

    # Tar bort anteckningen
    delete_response = client.delete(f"/notes/{note_id}")
    assert delete_response.status_code == 200
    assert delete_response.get_json()["message"] == f"Note {note_id} deleted"

    # Kollar så att den verkligen är borta
    get_response = client.get("/notes")
    notes = get_response.get_json()
    assert all(n["id"] != note_id for n in notes)
    
def test_create_note_with_script_tags(client):
    response = client.post("/notes", json={
        "title": "<script>alert('xss')</script>",
        "content": "<script>alert('xss')</script>"
    })
    assert response.status_code == 400

def test_create_note_with_empty_fields(client):
    response = client.post("/notes", json={
        "title": "",
        "content": ""
    })
    assert response.status_code == 400