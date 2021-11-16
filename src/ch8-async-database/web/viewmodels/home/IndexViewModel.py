from typing import List
from starlette.requests import Request
from web.viewmodels.base.BaseViewModel import BaseViewModel
from app.services.PackageService import PackageService
from app.services.UserService import UserService
from app.models.Package import Package

class IndexViewModel(BaseViewModel):

    def __init__(self, request: Request):
        super().__init__(request)
        self.package_count: int = 0
        self.release_count: int = 0
        self.user_count: int = 0
        self.packages: List[Package] = []

    async def load(self):
        self.package_count: int = await PackageService.get_package_count()
        self.release_count: int = await PackageService.get_release_count()
        self.user_count: int = await UserService.get_user_count()
        self.packages: List = await PackageService.get_latest_packages(limit= 7)  
        

