from external.dataBase.database_manager import DatabaseManager
from models.book import Book
class BookService():
    def __init__(self,databaseManager: DatabaseManager):
        self.databaseManager= databaseManager

    def create_book(self, book: Book):
            self.databaseManager.upsertBook(book)
            return book

    def list_books(self):
        return self.databaseManager.listAllBooks()

    def get_books(self,title: str | None = None, author: str | None = None,genre: str | None = None,isbn: str | None = None):
        return self.databaseManager.searchBook(title,author,genre,isbn)

    def delete_book(self, isbn):
            return self.databaseManager.eraseBook(isbn)