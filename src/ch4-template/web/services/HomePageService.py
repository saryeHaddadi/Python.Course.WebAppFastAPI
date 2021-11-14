import fastapi
from starlette.responses import HTMLResponse
from fastapi_chameleon import template


router = fastapi.APIRouter()


@router.get('/', response_class=HTMLResponse, include_in_schema=False)
@template('templates/home/index.pt')
def index():
    return {
        'package_count': 274_000,
        'release_count': 2_234_847,
        'user_count': 73_874,
        'packages': [
            {'id': 'fastapi', 'summary': "A great web framework"},
            {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
            {'id': 'httpx', 'summary': "Requests for an async world"},
        ]
    }


@router.get('/about')
@template()
def about():
    return {}
