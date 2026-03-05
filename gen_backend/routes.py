from fastapi import APIRouter, Response

from gen_backend.databases.gen_backend import Session
from gen_backend.handlers import create_registration
from gen_backend.schemas import RegistrationCreate

router = APIRouter()


@router.get("/health", status_code=200)
async def health():
    return Response(status_code=200)


@router.post("/api/registrations")
async def register(data: RegistrationCreate):
    async with Session() as session:
        registration = await create_registration(session, data)
        return {"id": registration.id}
