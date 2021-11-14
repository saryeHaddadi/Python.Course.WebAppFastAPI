import fastapi
from web.services import IndexPageService


class StartupApp:
    def __init__(self):
        self.app = None
        
    def create_app(self):
        self.app = fastapi.FastAPI()
        self.configure_app()
        return self.app

    def configure_app(self):
        self.configure_routing()

    def configure_routing(self):
        self.app.include_router(IndexPageService.router)

