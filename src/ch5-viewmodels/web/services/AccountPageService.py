import fastapi
from starlette.requests import Request
from web.viewmodels.account.AccountViewModel import AccountViewModel
from web.viewmodels.account.LoginViewModel import LoginViewModel
from web.viewmodels.account.RegisterViewModel import RegisterViewModel

router = fastapi.APIRouter()


@router.get('/account')
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout():
    return {}
