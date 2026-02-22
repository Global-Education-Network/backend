# gen-backend

FastAPI backend with async SQLAlchemy and Alembic migrations.

## Setup

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

## Environment Variables

| Variable | Description |
|---|---|
| `DATABASE_URL` | Full database URL (takes priority) |
| `CONTENT_DB_HOST` | Database host (fallback) |
| `CONTENT_DB_USER` | Database user (fallback) |
| `CONTENT_DB_PASSWORD` | Database password (fallback) |
| `CONTENT_DB_DATABASE` | Database name (fallback) |

## Migrations

```bash
alembic revision --autogenerate -m "migration message"
alembic upgrade head
```

## Run

```bash
uvicorn gen_backend.main:app --reload
```
