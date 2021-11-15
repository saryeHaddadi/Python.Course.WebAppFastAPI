from typing import List
from starlette.requests import Request
from web.viewmodels.shared.BaseViewModel import BaseViewModel
from app.services.PackageService import PackageService
from app.services.UserService import UserService

class IndexViewModel(BaseViewModel):

    def __init__(self, request: Request):
        super().__init__(request)

        self.package_count: int = PackageService.get_package_count()
        self.release_count: int = PackageService.get_release_count()
        self.user_count: int = UserService.get_user_count()
        self.packages: List = PackageService.get_latest_packages(limit= 5)  
        

