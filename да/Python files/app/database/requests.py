from app.database.models import async_session
from app.database.models import User
from sqlalchemy import select

import app.handlers as hdl

async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            session.add(User(health=100))
            await session.commit()

async def user_number(tg_id: int) -> None:

    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if user == user:
           user_pk = await session.get()
           await session.commit()
            