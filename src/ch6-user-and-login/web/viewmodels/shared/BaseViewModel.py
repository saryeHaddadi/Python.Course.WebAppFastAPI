from typing import Optional
from starlette.requests import Request
from infra.cookie import cookie_auth

class BaseViewModel:
    
    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None
        
        # Will be set throught cookies
        self.is_logged_in = cookie_auth.get_user_id_from_auth_cookie(self.request)
        
    def to_dict(self) -> dict:
        return self.__dict__




