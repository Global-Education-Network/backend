import os


def create_db_url(prefix: str, asynchronous=True) -> str:
    connector = "postgresql+asyncpg" if asynchronous else "postgresql"
    host = os.environ[f"{prefix}_HOST"]
    user = os.environ[f"{prefix}_USER"]
    password = os.environ[f"{prefix}_PASSWORD"]
    database = os.environ[f"{prefix}_DATABASE"]
    return f"{connector}://{user}:{password}@{host}:5432/{database}"


__all__ = ["gen_backend", "create_db_url"]