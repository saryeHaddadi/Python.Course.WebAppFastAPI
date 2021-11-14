import fastapi
from starlette.requests import Request
from starlette.responses import HTMLResponse
from fastapi_chameleon import template
from web.viewmodels.packages.DetailsViewModel import DetailModelBase

router = fastapi.APIRouter()

@router.get('/project/{package_name}', response_class=HTMLResponse, include_in_schema=False)
@template('packages/details.pt')
def about(package_name: str, request: Request):
    vm = DetailModelBase(package_name, request)
    return vm.to_dict()



