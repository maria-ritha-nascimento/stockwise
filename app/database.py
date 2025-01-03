from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./stockwise.db"  # Alterar conforme necessário para outros bancos

# Criação do engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Sessão de conexão com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para modelos do SQLAlchemy
Base = declarative_base()

# Função para criar tabelas
def create_tables():
    Base.metadata.create_all(bind=engine)

# Função para obter uma sessão de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
