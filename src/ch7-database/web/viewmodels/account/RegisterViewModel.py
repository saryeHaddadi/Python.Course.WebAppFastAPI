from typing import Optional
from starlette.requests import Request
from web.viewmodels.base.BaseViewModel import BaseViewModel
from app.services.UserService import UserService


class RegisterViewModel(BaseViewModel):

    def __init__(self, request: Request):
        super().__init__(request)
        
        self.name: Optional[str] = None
        self.password: Optional[str] = None
        self.email: Optional[str] = None

    async def load_and_validate(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.password = form.get('password')
        self.email = form.get('email')

        if self.validate_field(self.name):
            self.error = 'Your name is required'
        elif self.validate_field(self.password) or len(self.password) < 5:
            self.error = 'Your password is required and must be at 5 characters.'
        elif self.validate_field(self.email):
            self.error = 'Your email is required'
        elif UserService.get_user_by_email(self.email):
            self.error = "That email is already taken. Log in instead?"

    def validate_field(self, field: str):
        return (not self.name or not self.name.strip())
        





