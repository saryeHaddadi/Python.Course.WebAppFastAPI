import fastapi
import fastapi_chameleon
from starlette.staticfiles import StaticFiles
from web.services import HomePageService, PackagesPageService, AccountPageService
from web.config import PAGES_PATH, STATIC_PATH

class Startup:
    def __init__(self):
        self.app = None
        
    def create_app(self):
        self.app = fastapi.FastAPI()
        self.configure()
        return self.app

    def configure(self):
        self.configure_routing()
        self.configure_template()
        self.configure_mounts()

    def configure_template(self):
        fastapi_chameleon.global_init(str(PAGES_PATH))

    def configure_routing(self):
        self.app.include_router(HomePageService.router)
        self.app.include_router(PackagesPageService.router)
        self.app.include_router(AccountPageService.router)

    def configure_mounts(self):
        self.app.mount('/static', StaticFiles(directory=STATIC_PATH), name='static')
        
        
        