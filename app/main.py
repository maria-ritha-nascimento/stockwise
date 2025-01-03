from fastapi import FastAPI

from app.routes import items
from app.database import create_tables

# Instância principal da aplicação
app = FastAPI(title="StockWise", description="Sistema de Gestão de Estoque", version="1.0")

# Inicializa as tabelas no banco de dados
@app.on_event("startup")
def startup_event():
    create_tables()

# Inclui as rotas de itens
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao StockWise!"}
