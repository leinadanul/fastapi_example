from abc import ABC
from typing import List

#from models.book import Book 
from models.client import Client


class DatabaseManager (ABC):
    

        
    def addClient(self, client: Client) -> Client:
        pass
    def listAllClients(self)->List[Client]:
        pass