from fastapi import FastAPI
from external.dataBase.implementations.psycopg_impl import PsycopgDBManagerImpl
from models.book import Book
from services.books_services import BookService


app = FastAPI()

dbmanager = PsycopgDBManagerImpl()
bookService = BookService(dbmanager)

@app.post("/books")
async def create_book(book: Book):
        return bookService.create_book(book)

@app.get("/books")
async def list_books():
        return bookService.list_books()

@app.get("/books/search")
async def get_books(title: str | None = None, author: str | None = None, genre: str | None = None):
        return bookService.get_books(title= title,author= author,genre= genre)

@app.get("/books/{isbn}")
async def get_books(isbn : str):
        return bookService.get_books(isbn=isbn)

@app.delete("/books/{isbn}")
async def delete_book(isbn : str):
        return bookService.delete_book(isbn)


# Iniciar el servidor con Uvicorn
if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)