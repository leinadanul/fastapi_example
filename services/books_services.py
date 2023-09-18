import psycopg2
from external.dataBase.database_manager import DatabaseManager
from models.book import Book
from models.client import Client
from services import client_services
from services.client_services import ClientService
class BookService():
    def __init__(self,databaseManager: DatabaseManager):
        self.databaseManager= databaseManager
        self.connection = psycopg2.connect("dbname=library user=postgres password=toor port=5432 ")
        

        

    def create_book(self, book: Book):
            self.databaseManager.upsertBook(book)
            return book

    def list_books(self):
        return self.databaseManager.listAllBooks()

    def get_books(self,title: str | None = None, author: str | None = None,genre: str | None = None,isbn: str | None = None):
        return self.databaseManager.searchBook(title,author,genre,isbn)

    def delete_book(self, isbn):
            return self.databaseManager.eraseBook(isbn)
    


    def rent_book(self, client_id: int, isbn: str):
        client_service = ClientService(self.databaseManager)

        book = self.get_books(isbn=isbn)
        if not book:
            return " The book does not exist or is not available for rent"

        client = client_service.get_client(client_id)
        if not client:
            return "Client not found."

        if isbn in client.rented_books:
            return "The client is already renting this book ."

        client.rented_books.append(isbn)
        book.copies -= 1

        return self.databaseManager.getClient()