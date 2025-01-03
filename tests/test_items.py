import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

# Configurar o banco de dados de teste (SQLite em memória)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_stockwise.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependência para substituir o banco de dados no teste
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Substituir o banco de dados principal pelo de teste
app.dependency_overrides[get_db] = override_get_db

# Cria as tabelas no banco de dados de teste
Base.metadata.create_all(bind=engine)

# Instância do TestClient
client = TestClient(app)

# Testes unitários
def test_create_item():
    response = client.post("/items/", json={
        "name": "Teste Item",
        "description": "Descrição do item de teste",
        "quantity": 10,
        "price": 15.5
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Teste Item"
    assert data["description"] == "Descrição do item de teste"
    assert data["quantity"] == 10
    assert data["price"] == 15.5

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_item_by_id():
    # Primeiro criamos um item para testar
    response = client.post("/items/", json={
        "name": "Item para Teste",
        "description": "Descrição do item",
        "quantity": 5,
        "price": 9.99
    })
    assert response.status_code == 200
    created_item = response.json()

    # Buscar o item pelo ID
    response = client.get(f"/items/{created_item['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == created_item["id"]

def test_update_item():
    # Criar um item para testar a atualização
    response = client.post("/items/", json={
        "name": "Item Atualizar",
        "description": "Descrição antes da atualização",
        "quantity": 2,
        "price": 5.0
    })
    assert response.status_code == 200
    created_item = response.json()

    # Atualizar o item
    response = client.put(f"/items/{created_item['id']}", json={
        "name": "Item Atualizado",
        "description": "Descrição atualizada",
        "quantity": 20,
        "price": 10.0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Item Atualizado"
    assert data["description"] == "Descrição atualizada"
    assert data["quantity"] == 20
    assert data["price"] == 10.0

def test_delete_item():
    # Criar um item para testar a exclusão
    response = client.post("/items/", json={
        "name": "Item Deletar",
        "description": "Será excluído",
        "quantity": 1,
        "price": 1.0
    })
    assert response.status_code == 200
    created_item = response.json()

    # Deletar o item
    response = client.delete(f"/items/{created_item['id']}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Item {created_item['id']} deleted successfully"}

    # Verificar se o item não existe mais
    response = client.get(f"/items/{created_item['id']}")
    assert response.status_code == 404
