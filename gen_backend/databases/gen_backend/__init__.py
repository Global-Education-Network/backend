import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from gen_backend.databases import create_db_url

if env_db_url := os.environ.get("DATABASE_URL"):
    SYNC_DB_URL = env_db_url
    DB_URL = env_db_url.replace("postgres://", "postgresql+asyncpg://")
else:
    SYNC_DB_URL = create_db_url("GEN_BACKEND_DB", asynchronous=False)
    DB_URL = create_db_url("GEN_BACKEND_DB")

engine = create_async_engine(
    DB_URL,
    pool_size=int(os.environ.get("DB_CONN_POOL_SIZE", 4)),
    max_overflow=int(os.environ.get("DB_CONN_POOL_MAX_OVERFLOW", 0)),
    pool_timeout=120,
)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=AsyncSession)  # noqa

__all__ = ["Session", "engine", "models", "DB_URL", "SYNC_DB_URL"]
