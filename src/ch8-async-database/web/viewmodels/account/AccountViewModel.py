from typing import Optional
from starlette.requests import Request
from web.viewmodels.base.BaseViewModel import BaseViewModel
from app.models.User import User
from app.services.UserService import UserService

class AccountViewModel(BaseViewModel):

    def __init__(self, request: Request):
        super().__init__(request)
        
        self.user = Optional[User]

    async def load(self):
        self.user = await UserService.get_user_by_id(self.user_id)

