from fastapi import FastAPI
#from external.dataBase.implementations.psycopg_impl import PsycopgDBManagerImpl
from external.dataBase.implementations.sqlalchemy_implementation import SQLAlchemyDBManager

from models.client import Client

from services.client_service_two import ClientService


app = FastAPI()


db_manage = SQLAlchemyDBManager()
#dbmanager = PsycopgDBManagerImpl()
#bookService = BookService(dbmanager)
clientService = ClientService(db_manage)

@app.get("/clients")
async def list_clients():
        return clientService.list_clients()


# Iniciar el servidor con Uvicorn
if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)