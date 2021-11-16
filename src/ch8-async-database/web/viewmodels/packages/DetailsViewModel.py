from typing import Optional
from starlette.requests import Request
from web.viewmodels.base.BaseViewModel import BaseViewModel
from app.services.PackageService import PackageService
from app.models.Release import Release
from app.models.Package import Package

class DetailModelBase(BaseViewModel):

    def __init__(self, package_name: str, request: Request):
        super().__init__(request)
        
        self.package_name: str = package_name
        self.is_latest = True
        self.maintainers = []
        self.package: Optional[Package] = None
        self.latest_release: Optional[Release] = None
        self.latest_version: str = None
        
    async def load(self):
        self.package = await PackageService.get_package_by_id(self.package_name)
        self.latest_release = await PackageService.get_latest_release_for_package(self.package_name)
        
        if not self.package or not self.latest_release:
            return

        self.latest_version = self.latest_release.version_text
        
        
