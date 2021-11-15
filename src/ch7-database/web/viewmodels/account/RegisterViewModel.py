from typing import Optional
from starlette.requests import Request
from web.viewmodels.shared.BaseViewModel import BaseViewModel
from app.models.User import User

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
            
        if self.validate_field(self.password):
            self.error = 'Your password is required'
            
        if self.validate_field(self.email):
            self.error = 'Your email is required'

    def validate_field(self, field: str):
        return (not self.name or not self.name.strip())
        





