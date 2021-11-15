# TODO: reference to app.core.repository
from typing import Optional
from app.models.User import User


class UserService:
    
    def get_user_count():
        return 73_874

    def create_account(name: str, email: str, password: str) -> User:
        return User(name, email, 'abc')

    def login_user(email: str, password: str) -> Optional[User]:
        if password == 'abc':
            return User("test user", email, 'abc')

        return None



