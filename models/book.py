
from pydantic import BaseModel, Field


class Book(BaseModel):
    isbn: str = Field (...,min_length=13, max_length=13, pattern="^[0-9]*$") 
    title: str
    author: str
    genre: str
    copies: int
