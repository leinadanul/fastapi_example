from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from external.dataBase.database_manager import DatabaseManager
from models.client import Client

Base = declarative_base()

class SQLAlchemyDBManager(DatabaseManager):
    def __init__(self):
        self.engine = create_engine("postgresql://postgres:toor@localhost:5432/alchemy")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()






    def addClient(self, client: Client) -> Client:
        self.session.add(client)
        self.session.commit()
        return client
'''
    def listAllClients(self) -> List[Client]:
        return self.session.query(Client).all()

    def upsertBook(self, book: Book) -> Book:
        existing_book = self.session.query(Book).filter_by(isbn=book.isbn).first()
        if existing_book:
            existing_book.copies += book.copies
            self.session.commit()
            return existing_book
        else:
            self.session.add(book)
            self.session.commit()
            return book

    def listAllBooks(self) -> List[Book]:
        return self.session.query(Book).all()

    def searchBook(self, title: str | None = None, author: str | None = None, genre: str | None = None, isbn: str | None = None) -> List[Book]:
        query = self.session.query(Book)
        if isbn:
            query = query.filter(Book.isbn == isbn)
        if title:
            query = query.filter(Book.title.ilike(f'%{title}%'))
        if author:
            query = query.filter(Book.author.ilike(f'%{author}%'))
        if genre:
            query = query.filter(Book.genre.ilike(f'%{genre}%'))
        return query.all()

    def eraseBook(self, isbn: str) -> str:
        book = self.session.query(Book).filter_by(isbn=isbn).first()
        if book:
            self.session.delete(book)
            self.session.commit()
            return f'The book with {isbn} has been deleted.'
        else:
            return f'The book with {isbn} was not found.'
            '''