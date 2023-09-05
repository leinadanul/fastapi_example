'''from pydantic import BaseModel, Field


class Client(BaseModel):
    id: int 
    name: str =Field(min_length=3)
    '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String)