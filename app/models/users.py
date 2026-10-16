import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Uuid 

from app.database.db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, index=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(225), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(225))




