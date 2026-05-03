from models import Book

def test_book_creation():
    book = Book(title="Test", author="Author")
    assert book.title == "Test"