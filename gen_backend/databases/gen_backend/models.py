from sqlalchemy import BigInteger, Boolean, Column, DateTime, Numeric, String, func
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at = Column(DateTime, nullable=True)


class Registration(Base):
    __tablename__ = "registrations"

    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    country_dialing_code = Column(String, nullable=True)
    contact = Column(String, nullable=True)
    contributions = Column(ARRAY(String), nullable=False)
    donation_commitment = Column(Numeric, nullable=True)
    currency = Column(String, nullable=True)
    contact_permission = Column(Boolean, nullable=False)
    feedback = Column(String, nullable=True)
