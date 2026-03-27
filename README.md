# 🚀 Fast Zero - FastAPI & PostgreSQL Project

Modern, production-ready FastAPI project with automated Docker orchestration and PostgreSQL integration.

---

## 🛠️ Technology Stack

- **[FastAPI](https://fastapi.tiangolo.com/)**: High-performance Python web framework.
- **[PostgreSQL](https://www.postgresql.org/)**: Robust and scalable relational database.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Advanced ORM with async support.
- **[Alembic](https://alembic.sqlalchemy.org/)**: Precise database migrations.
- **[Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)**: Full container orchestration.
- **[Pytest](https://docs.pytest.org/)**: Comprehensive test suite with [Testcontainers](https://testcontainers.com/).
- **[Ruff](https://beta.ruff.rs/)**: Ultra-fast linting and formatting.

---

## 🏗️ Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Poetry](https://python-poetry.org/) (optional, for local dev)

---

## 🚀 Getting Started (Docker - Recommended)

The easiest way to run the project on any machine is via Docker Compose:

1. **Clone the repository**:

   ```bash
   git clone <repo-url>
   cd fast-api
   ```

2. **Start the environment**:
   ```bash
   docker compose up -d --build
   ```

This command builds the application, starts a PostgreSQL instance, and automatically runs all database migrations. The API will be available at [http://localhost:8000](http://localhost:8000).

---

## 🧪 Running Tests

Tests are automated using **Testcontainers**, which spins up an ephemeral PostgreSQL instance on the fly. To run the tests, you must have Docker running:

```bash
task test
```

---

## 🛠️ Local Development (Manual Setup)

1. **Install dependencies**:

   ```bash
   poetry install
   ```

2. **Configure Environment**:
   Ensure your `.env` file points to a running PostgreSQL instance.

3. **Useful Commands (via Taskipy)**:
   - `task run`: Start local development server.
   - `task test`: Execute all tests (with coverage).
   - `task lint`: Check code quality with Ruff.
   - `task format`: Auto-format code.
   - `task alembic`: Database migration commands.

---

## 🗄️ Database Migrations

Migrations are automated via `entrypoint.sh` in Docker, but can be managed manually:

```bash
# Inside the app container
docker compose exec fastzero_app poetry run alembic upgrade head

# Or locally
task alembic upgrade head
```

---

## 📝 Author

Created with ⚡ by **andsantosx**.
