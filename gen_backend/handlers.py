from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from gen_backend.databases.gen_backend.models import Registration
from gen_backend.schemas import RegistrationCreate


async def create_registration(session: AsyncSession, data: RegistrationCreate) -> Registration:
    try:
        registration = Registration(**data.model_dump())
        session.add(registration)
        await session.commit()
        await session.refresh(registration)
        return registration
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=409, detail="A registration with this email already exists")
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
