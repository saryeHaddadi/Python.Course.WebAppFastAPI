import fastapi
from starlette.requests import Request
from starlette import status
from fastapi_chameleon import template
from web.viewmodels.account.AccountViewModel import AccountViewModel
from web.viewmodels.account.LoginViewModel import LoginViewModel
from web.viewmodels.account.RegisterViewModel import RegisterViewModel
from app.services.UserService import UserService
from infra.cookie import cookie_auth

router = fastapi.APIRouter()


@router.get('/account')
@template('account/index.pt')
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
@template('account/register.pt')
def register_get(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()

@router.post('/account/register')
@template('account/register.pt')
async def register_post(request: Request):
    vm = RegisterViewModel(request)
    await vm.load_and_validate()
    
    if vm.error:
        return vm.to_dict()
    
    account = UserService.create_account(vm.name, vm.email, vm.password)
    
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)
    
    return response


@router.get('/account/login')
@template('account/login.pt')
def login_get(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login')
@template(template_file='account/login.pt')
async def login_post(request: Request):

    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = UserService.login_user(vm.email, vm.password)
    if not user:
        vm.error = "The account does not exist or the password is wrong."
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.id)

    return resp


@router.get('/account/logout')
def logout():
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)
    return response
