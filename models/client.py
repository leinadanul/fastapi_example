from pydantic import BaseModel, Field
from typing import List


class Client(BaseModel):
    id: int 
    name: str =Field(min_length=3)
    rented_book: list[str] = []
    