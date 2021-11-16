import fastapi
from starlette.requests import Request
from starlette.responses import HTMLResponse
from http import HTTPStatus
from fastapi_chameleon import template
from web.viewmodels.home.IndexViewModel import IndexViewModel
from web.viewmodels.base.BaseViewModel import BaseViewModel

router = fastapi.APIRouter()

@router.get('/', response_class=HTMLResponse, include_in_schema=False)
@template('home/index.pt')
async def index(request: Request):
    vm = IndexViewModel(request)
    await vm.load()
    return vm.to_dict()

@router.get('/about')
@template('home/about.pt')
def about(request: Request):
    vm = BaseViewModel(request)
    return vm.to_dict()

@router.get('/favicon.ico', include_in_schema=False)
def favicon():
    # /static should be mounted
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico',
                                              status_code=HTTPStatus.PERMANENT_REDIRECT)



