from sqlalchemy.ext.asyncio import AsyncSession

from gen_backend.databases.gen_backend.models import Registration
from gen_backend.schemas import RegistrationCreate


async def create_registration(session: AsyncSession, data: RegistrationCreate) -> Registration:
    registration = Registration(**data.model_dump())
    session.add(registration)
    await session.commit()
    await session.refresh(registration)
    return registration
