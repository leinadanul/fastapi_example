
from fastapi.testclient import TestClient



from ..main import app

client = TestClient(app)

def test_create_book():
    book_data = {
        "isbn": "1234567890123",
        "title": "shrek",
        "author": "shrek",
        "genre": "comedy",
        "copies": 10
    }
    response = client.post("/books", json=book_data)
    assert response.status_code == 200
    assert response.json() == book_data



def test_create_book_with_invalid_isbn():
    book_data= {
    "isbn": "802310682634289797",
    "title": "string",
    "author": "string",
    "genre": "string",
    "copies": 0
    }
    response = client.post("/books", json=book_data)
    assert response.status_code == 422
"""Pending to ask what should i do here"""



def test_create_book_with_valid_isbn():
    book_data = {
        "isbn": "1234567890123", 
        "title": "shrek",
        "author": "shrek",
        "genre": "comedy",
        "copies": 10
    }
    response = client.post("/books", json=book_data)
    assert response.status_code == 200
    assert response.json() == book_data