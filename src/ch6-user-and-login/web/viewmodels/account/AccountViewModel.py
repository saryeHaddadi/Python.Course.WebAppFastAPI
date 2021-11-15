from starlette.requests import Request
from web.viewmodels.shared.BaseViewModel import BaseViewModel
from infra.data.User import User

class AccountViewModel(BaseViewModel):

    def __init__(self, request: Request):
        super().__init__(request)
        
        self.user = User('Michael', 'michael@live.de', 'skfdf,(kog,')


