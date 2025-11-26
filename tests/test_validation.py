from src.validation import validate_note_input

def test_valid_note():
    valid_note = {"title": "Min titel", "content": "Innehåll"}
    assert validate_note_input(valid_note) is True

def test_invalid_note_missing_title():
    invalid_note = {"content": "Innehåll"}
    assert validate_note_input(invalid_note) is False

def test_invalid_note_with_script():
    invalid_note = {"title": "<script>alert('XSS')</script>", "content": "Innehåll"}
    assert validate_note_input(invalid_note) is False
