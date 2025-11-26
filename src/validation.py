def is_valid_note(title, content):
    if not title or not content:
        return False
    if "<script>" in title.lower() or "<script>" in content.lower():
        return False
    return True
