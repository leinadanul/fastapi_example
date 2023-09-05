from pydantic import BaseModel, Field


class Client(BaseModel):
    id: int 
    name: str =Field(min_length=3)
    