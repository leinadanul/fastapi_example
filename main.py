from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import sqlalchemy as db
import psycopg2







app = FastAPI()

# Modelo para libros
class Book(BaseModel):
    isbn: int
    title: str
    author: str
    genre: str
    copies: int

# Simulación de una base de datos

connection = psycopg2.connect("dbname=library user=postgres password=toor port=5432  ")





'''user = "postgres"
password = "toor"
database = "library"
server = "localhost"
port = "5432"

db_url = f"postgresql+psycopg2://{user}:{password}@{server}:{port}/{database}"

engine = db.create_engine(db_url)



connection = engine.connect()
metadata = db.MetaData()
book = db.Table('book', metadata, autoload=True, autoload_with=engine)
'''



#Equivalent to 'SELECT * FROM census'







'''=========================================================================='''

@app.post("/books")
async def create_book(book: Book):
        cur = connection.cursor()
        cur.execute("""INSERT INTO book(
	isbn, title, author, genre, copies)
	VALUES (%(isbn)s, %(title)s, %(author)s, %(genre)s, %(copies)s);""",
    {'isbn':book.isbn, 'title': book.title, 'author': book.author, 'genre': book.genre, 'copies': book.copies})
        connection.commit()
        cur.close()
        return book


@app.get("/books")
async def list_books():
    cur = connection.cursor()
    cur.execute("SELECT * FROM book")
    getBook = cur.fetchall()
    cur.close
    return getBook

'''
@app.get("/books/search")
async def get_book_by_title(title: str | None = None, author: str | None = None):
    list = []
    if title:
        for book in books_db:
            if title in book.title:
                list.append(book)
    if author:
        for book in books_db:
            if author in book.author:
                list.append(book)
    return list

@app.get("/books/{isbn}")
async def get_book_by_isbn(isbn: int):
    book_list = []
    for book in books_db:
        if book.isbn == isbn:
            book_list.append(book)
    return book_list


'''





# Iniciar el servidor con Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)