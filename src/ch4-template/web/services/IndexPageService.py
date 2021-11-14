import fastapi

router = fastapi.APIRouter()

@router.get('/')
def index():
    return {"message": "Hello"}


