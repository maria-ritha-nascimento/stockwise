# StockWise

**StockWise** é um sistema de gestão de estoque desenvolvido em Python usando o framework FastAPI. Ele permite gerenciar itens de forma eficiente, incluindo operações como criar, listar, atualizar e deletar produtos. O sistema utiliza um banco de dados SQLite para armazenamento local e é ideal para pequenas e médias empresas que desejam monitorar seus estoques com facilidade.

---

## 📖 **Descrição Técnica**

O **StockWise** foi construído seguindo boas práticas de desenvolvimento, incluindo:
- **FastAPI**: Para construção dos endpoints RESTful.
- **SQLAlchemy**: Como ORM (Object-Relational Mapping) para interação com o banco de dados.
- **SQLite**: Banco de dados relacional para persistência.
- **Pydantic**: Para validação e serialização de dados.
- **pytest**: Para testes automatizados e garantia da qualidade do código.

O projeto adota uma arquitetura modular, com separação de responsabilidades entre rotas, modelos e configuração de banco de dados.

---

## 🚀 **Como Executar o Projeto**

Siga os passos abaixo para configurar e executar o projeto em sua máquina:

### **Pré-requisitos**
- Python 3.10 ou superior
- Git para clonar o repositório

### **Passos de Instalação**

1. **Clone o repositório**
   ```bash
   git clone https://github.com/maria-ritha-nascimento/stockwise.git
   cd stockwise
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o banco de dados**
   Inicie o banco de dados e crie as tabelas necessárias:
   ```bash
   python -c "from app.database import create_tables; create_tables()"
   ```

5. **Execute o servidor**
   Inicie o servidor FastAPI:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Acesse o sistema**
   O sistema estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

   A documentação interativa da API pode ser acessada em:
   - Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 **Testes Automatizados**

Para garantir o bom funcionamento do sistema, foram implementados testes unitários. Siga os passos abaixo para executá-los:

1. Ative o ambiente virtual (caso ainda não esteja ativo).
2. Execute os testes:
   ```bash
   pytest
   ```
3. Certifique-se de que todos os testes passaram antes de usar o sistema em produção.

---

## 🛠️ **Tecnologias Utilizadas**

- **Linguagem**: Python 3.10+
- **Framework**: FastAPI
- **Banco de Dados**: SQLite
- **ORM**: SQLAlchemy
- **Validação**: Pydantic
- **Testes**: pytest

---

## 🤝 **Contribuição**

Sinta-se à vontade para contribuir com o **StockWise**! Sugestões, correções e melhorias são sempre bem-vindas. Para contribuir:
1. Faça um fork do repositório.
2. Crie um branch para a sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das alterações:
   ```bash
   git commit -m "Descrição da alteração"
   ```
4. Envie para o branch principal:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## 📞 **Suporte**

Se você tiver alguma dúvida ou problema, entre em contato:
- **GitHub Issues**: [Acesse aqui](https://github.com/maria-ritha-nascimento/stockwise/issues)
