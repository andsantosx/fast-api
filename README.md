# Fast Zero - FastAPI Project

Um projeto de estudo FastAPI.

## Tecnologias e Recursos

- **FastAPI**: Framework web moderno e rápido.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **Alembic**: Gerenciamento de migrações de banco de dados.
- **SQLite**: Banco de dados leve para desenvolvimento e testes.
- **Ruff**: Linting e formatação ultra-rápida.
- **Pytest**: Suíte de testes automatizados com **100% de cobertura**.

## Como rodar

1. Instale o [Poetry](https://python-poetry.org/) se ainda não tiver.
2. Instale as dependências:
   ```bash
   poetry install
   ```
3. Execute as migrações:
   ```bash
   task alembic upgrade head
   ```
4. Rode o servidor:
   ```bash
   task run
   ```

## Comandos úteis (Taskipy)

- `task run`: Inicia o servidor de desenvolvimento.
- `task test`: Executa os testes com cobertura (100% atual).
- `task lint`: Verifica o código com Ruff.
- `task format`: Formata o código automaticamente.
- `task alembic`: Atalho para comandos do Alembic.
