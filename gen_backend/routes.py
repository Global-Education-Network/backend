from fastapi import APIRouter

from gen_backend.databases.gen_backend import Session
from gen_backend.handlers import create_registration
from gen_backend.schemas import RegistrationCreate

router = APIRouter()


@router.post("/registrations")
async def register(data: RegistrationCreate):
    async with Session() as session:
        registration = await create_registration(session, data)
        return {"id": registration.id}
