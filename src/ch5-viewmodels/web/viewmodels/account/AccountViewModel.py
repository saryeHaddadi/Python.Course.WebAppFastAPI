from starlette.requests import Request
from web.viewmodels.shared.BaseViewModel import BaseViewModel


class AccountViewModel(BaseViewModel):

    def __init__(self, request: Request):
        super().__init__(request)


