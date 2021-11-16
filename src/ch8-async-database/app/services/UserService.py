# TODO: reference to app.core.repository
from typing import Optional
from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from app.models.User import User
from infra.data import db_session

class UserService:
    
    def get_user_count():
        session = db_session.create_session()
        try:
            return session.query(User).count()
        finally:
            session.close()

    def create_account(name: str, email: str, password: str) -> User:
        session = db_session.create_session()
        try:
            user = User()
            user.email = email
            user.name = name
            user.hash_password = crypto.hash(password, rounds=1_000) # 200_000
            
            session.add(user)
            session.commit()
            return user
        finally:
            session.close()

    def login_user(email: str, password: str) -> Optional[User]:
        user = UserService.get_user_by_email(email)
        if not user:
            return user
        
        if not crypto.verify(password, user.hash_password):
            return None
        return user
    
    def get_user_by_id(user_id: str) -> Optional[User]:
        session = db_session.create_session()
        try:
            return session.query(User).filter(User.id == user_id).first()
        finally:
            session.close()

    def get_user_by_email(email: str) -> Optional[User]:
        session = db_session.create_session()
        try:
            return session.query(User).filter(User.email == email).first()
        finally:
            session.close()