from abc import ABC
from typing import List

from models.book import Book 
from models.client import Client

class DatabaseManager (ABC):
    
    def upsertBook(self, book:Book)->Book:
        pass
    def listAllBooks(self)->List[Book]:
        pass
    def searchBook(self, title: str | None = None, author: str | None = None, genre: str| None = None, isbn: str| None= None)-> List[Book]:
        pass
    def eraseBook(self, isbn : str)->Book:
        pass
    def addClient(self, client: Client)->Client:
        pass
    def listAllClients(self)->List[Client]:
        pass
    def getClient(self, client_id: int) -> Client:
        pass