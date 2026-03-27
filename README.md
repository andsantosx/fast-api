# 🚀 Fast Zero - Projeto FastAPI & PostgreSQL

Projeto FastAPI moderno, pronto para produção, com orquestração Docker automatizada e integração com PostgreSQL.

---

## 🛠️ Stack Tecnológica

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web Python de alta performance.
- **[PostgreSQL](https://www.postgresql.org/)**: Banco de dados relacional robusto e escalável.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: ORM avançado com suporte assíncrono.
- **[Alembic](https://alembic.sqlalchemy.org/)**: Gerenciamento preciso de migrações de banco de dados.
- **[Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)**: Orquestração completa de containers.
- **[Pytest](https://docs.pytest.org/)**: Suíte de testes abrangente com [Testcontainers](https://testcontainers.com/).
- **[Ruff](https://beta.ruff.rs/)**: Linting e formatação ultra-rápidos.

---

## 🏗️ Pré-requisitos

Certifique-se de ter instalado:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/) (opcional, para desenvolvimento local)

---

## 🚀 Como Iniciar (Docker - Recomendado)

A maneira mais fácil de rodar o projeto em qualquer máquina é via Docker Compose:

1. **Clone o repositório**:

   ```bash
   git clone <repo-url>
   cd fast-api
   ```

2. **Configure o Ambiente**:
   - Copie o arquivo de exemplo:
     ```bash
     cp .env.example .env
     ```
   - Atualize os valores no `.env` se necessário (ex: `SECRET_KEY`).

3. **Inicie o ambiente**:
   ```bash
   docker compose up -d --build
   ```

Este comando constrói a aplicação, inicia uma instância do PostgreSQL e executa automaticamente todas as migrações do banco de dados. A API estará disponível em [http://localhost:8000](http://localhost:8000).

---

## 🔐 Configuração de Ambiente

O projeto utiliza um arquivo `.env` para todas as configurações sensíveis. O formato da `DATABASE_URL` para PostgreSQL é:

`DATABASE_URL="postgresql+psycopg://usuario:senha@host:porta/banco"`

### ⚡ Por que `localhost:5432`?

Ao rodar o projeto **localmente** (na sua máquina via `task run`), você usa `localhost:5432` porque o container Docker expõe a porta do banco de dados para a sua máquina.

### 🐳 Por que a auto-configuração do Docker funciona?

Ao rodar **dentro do Docker** (via `docker compose`), o sistema substitui automaticamente o host para `fastzero_database`. Isso significa que o **mesmo arquivo `.env`** funciona perfeitamente para ambos os ambientes, sem mudanças manuais! 🚀

---

## 🧪 Executando Testes

Os testes são automatizados usando **Testcontainers**, que sobe uma instância efêmera do PostgreSQL dinamicamente. Para rodar os testes, você deve ter o Docker rodando:

```bash
task test
```

---

## 🛠️ Desenvolvimento Local (Setup Manual)

1. **Instale as dependências**:

   ```bash
   poetry install
   ```

2. **Configure o Ambiente**:
   Certifique-se de que seu arquivo `.env` aponta para uma instância ativa do PostgreSQL.

3. **Comandos Úteis (via Taskipy)**:
   - `task run`: Inicia o servidor de desenvolvimento local.
   - `task test`: Executa todos os testes (com cobertura).
   - `task lint`: Verifica a qualidade do código com Ruff.
   - `task format`: Formata o código automaticamente.
   - `task alembic`: Comandos de migração do Alembic.

---

## 🗄️ Migrações de Banco de Dados

As migrações são automatizadas via `entrypoint.sh` no Docker, mas podem ser gerenciadas manualmente:

```bash
# Dentro do container da aplicação
docker compose exec fastzero_app poetry run alembic upgrade head

# Ou localmente
task alembic upgrade head
```

---

## 📝 Autor

Criado com ⚡ por **andsantosx**.
