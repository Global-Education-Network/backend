# gen-backend

FastAPI backend with async SQLAlchemy and Alembic migrations for Global Education Network (GEN), 
an NGO dedicated to providing free, quality education to students in medium and lower income countries.

## Setup

```bash
pip install -r requirements.txt
```

Create .env to store environment variables

## Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | Full database URL (takes priority) |
| `GEN_BACKEND_DB_HOST` | Database host (fallback) |
| `GEN_BACKEND_DB_USER` | Database user (fallback) |
| `GEN_BACKEND_DB_PASSWORD` | Database password (fallback) |
| `GEN_BACKEND_DB_DATABASE` | Database name (fallback) |

## Migrations

```bash
alembic revision --autogenerate -m "migration message"
alembic upgrade head
```

## Run

```bash
uvicorn gen_backend.main:app --reload
```
