from schemas import Book

def find_book(attr, attr_value, data):
    results = [(i, book) for i, book in enumerate(data) if getattr(book, attr) == attr_value]
    result = results[0] if results else None
    return result
    