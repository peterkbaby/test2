from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from pwdlib import PasswordHash

from app.schemas.users import UserCreate, UserResponse
from app.database.db import get_db
from app.models.users import User

pwd = PasswordHash.recommended()
router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):


    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = pwd.hash(user.password)
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
