from decimal import Decimal

from pydantic import BaseModel, EmailStr, Field


class RegistrationCreate(BaseModel):
    email: EmailStr
    name: str = Field(min_length=1)
    contact: str | None = None
    contributions: list[str] = Field(min_length=1)
    donation_commitment: Decimal | None = Field(default=None, gt=0)
    currency: str | None = Field(default=None, min_length=3, max_length=3)
    contact_permission: bool
    feedback: str | None = None
