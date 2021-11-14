from typing import Optional
from starlette.requests import Request

class BaseViewModel:
    
    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None
        # Will be set thourgh cookies
        self.is_logged_in = False
        
    def to_dict(self) -> dict:
        return self.__dict__




