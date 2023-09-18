from typing import List
import psycopg2
from external.dataBase.database_manager import DatabaseManager
from models.book import Book
from models.client import Client



class PsycopgDBManagerImpl(DatabaseManager):
        def __init__(self): 
            self.connection = psycopg2.connect("dbname=library user=postgres password=toor port=5432 ")
        
        def __mapResultToBooks(self, results: List[any]):
            books:List(Book)=[]
            for i in results:
                books.append(Book(isbn=i[0],title=i[1],author=i[2],genre=i[3],copies=i[4]))
            return books
        
        def __fetchBooks(self, query: str, value: str| None=None):
            cur = self.connection.cursor()
            if value:
                cur.execute(query, {'value': value})
            else:
                cur.execute(query)
            results = cur.fetchall()
            cur.close
            return results

        def addClient(self, client: Client) -> Client:
            cur = self.connection.cursor()
            cur.execute("""INSERT INTO client
                        (id,name) 
                        VALUES (%(id)s, %(name)s)""",
                        {'id': client.id, 'name': client.name})
            self.connection.commit()
            cur.close()
            return client
        
        def listAllClients(self) -> list[Client]:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM client")
            result = cur.fetchall()
            return result



        def upsertBook(self, book:Book)->Book:
            cur = self.connection.cursor()
            cur.execute("""INSERT INTO books(
        isbn, title, author, genre, copies)
        VALUES (%(isbn)s, %(title)s, %(author)s, %(genre)s, %(copies)s) ON CONFLICT (isbn) 
        DO UPDATE SET copies = books.copies + EXCLUDED.copies;""",
        {'isbn':book.isbn, 'title': book.title, 'author': book.author, 'genre': book.genre, 'copies': book.copies})
            self.connection.commit()
            cur.close()
            return book
        
        
        def listAllBooks(self)->List[Book]:
            results = self.__fetchBooks("SELECT * FROM books")
            return self.__mapResultToBooks(results)
        

        def searchBook(self, title: str | None = None, author: str | None = None, genre: str| None = None, isbn: str| None= None)->List[Book]:
            query : str = None
            value : str = None
            if isbn:
                query= """SELECT * FROM books WHERE isbn = %(value)s"""
                value = isbn
            if title:
                query= """SELECT * FROM books WHERE title like %(value)s"""
                value  = '%{}%'.format(title)
            if author:
                query= """SELECT * FROM books WHERE author like %(value)s"""
                value = '%{}%'.format(author)
            if genre:
                query= """SELECT * FROM books WHERE genre Like %(value)s"""
                value = '%{}%'.format(genre)
            print(value)
            results = self.__fetchBooks(query, value)
            return self.__mapResultToBooks(results)
        

        def eraseBook(self, isbn : str)->Book:
            cur = self.connection.cursor()
            cur.execute("DELETE FROM books WHERE isbn = %(isbn)s", {'isbn': isbn})
            self.connection.commit()
            cur.close()
            return f'The book with {isbn} was be delete'
        
        def getClient(self, client_id):
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM client WHERE id = %(id)s", {'id': client_id})
            result = cur.fetchone()
            cur.close()
            if result:
                client_id, client_name = result
                return Client(id=client_id, name=client_name)
            return None
    