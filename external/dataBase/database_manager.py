from abc import ABC
from typing import List

from models.book import Book 

class DatabaseManager (ABC):
    
    def upsertBook(self, book:Book)->Book:
        pass
    def listAllBooks(self)->List[Book]:
        pass
    def searchBook(self, title: str | None = None, author: str | None = None, genre: str| None = None, isbn: str| None= None)-> List[Book]:
        pass
    def eraseBook(self, isbn : str)->Book:
        pass