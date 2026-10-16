from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.db import engine, Base
from app.routers import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users.router)

