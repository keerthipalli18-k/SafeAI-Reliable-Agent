
def create_draft(title, content):

    if not title.strip():
        raise ValueError("Title cannot be empty")

    if not content.strip():
        raise ValueError("Content cannot be empty")

    draft = {
        "title": title,
        "content": content
    }

    return draft
