from external.dataBase.database_manager import DatabaseManager
from models.client import Client
from sqlalchemy.orm import sessionmaker
from external.dataBase.implementations.sqlalchemy_implementation import SQLAlchemyDBManager


db_manage = SQLAlchemyDBManager
class ClientService:
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager

    def create_client(self, client: Client):
        return self.database_manager.addClient(client)

    def list_clients(self):
        return self.database_manager.listAllClients()