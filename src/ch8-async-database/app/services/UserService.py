# TODO: reference to app.core.repository
from typing import Optional
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from app.models.User import User
from infra.data import db_session
from sqlalchemy.future import select
from sqlalchemy import func

class UserService:
    
    async def get_user_count():
        async with db_session.create_async_session() as session:
            query = select(func.count(User.id))
            result = await session.execute(query)
            return result.scalar_one_or_none()
    

    async def create_account(name: str, email: str, password: str) -> User:
        user = User()
        user.email = email
        user.name = name
        user.hash_password = crypto.hash(password, rounds=1_000) # rounds=200_000
        
        async with db_session.create_async_session() as session:
            session.add(user)
            await session.commit()
        
        return user

    async def login_user(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email)
        if not user:
            return user
        
        if not crypto.verify(password, user.hash_password):
            return None
        return user
    
    async def get_user_by_id(user_id: str) -> Optional[User]:
        async with db_session.create_async_session() as session:
            query = select(User).filter(User.id == user_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def get_user_by_email(email: str) -> Optional[User]:
        async with db_session.create_async_session() as session:
            query = select(User).filter(User.email == email)
            result = await session.execute(query)
            return result.scalar_one_or_none()
