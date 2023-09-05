import psycopg2
from external.dataBase.database_manager import DatabaseManager
from models.client import Client
class ClientService():
    def __init__(self,databaseManager: DatabaseManager):
        self.databaseManager= databaseManager
        self.connection = psycopg2.connect("dbname=library user=postgres password=toor port=5432 ")



    def create_client(self, client: Client):
        self.databaseManager.addClient(client)
        return client
    
    def list_clients(self):
        return self.databaseManager.listAllClients()
