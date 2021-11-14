from typing import List, Optional
import datetime
from infra.data.Package import Package
from infra.data.Release import Release

class PackageService:
    
    def get_package_count() -> int:
        return 274_000

    def get_release_count() -> int:
        return 2_234_847

    def get_latest_packages(limit: int = 5) -> List:
        return [
            {'id': 'fastapi', 'summary': "A great web framework"},
            {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
            {'id': 'httpx', 'summary': "Requests for an async world"},
        ][:limit]

    def get_package_by_id(package_name: str) -> Optional[Package]:
        package = Package(package_name= package_name,
                          summary="This is a summary",
                          description= "Cool description",
                          home_page= "https://fastapi.tiangolo.com",
                          license= "MIT",
                          author_name= "Sebastian Ramirez"
        )
        return package

    def get_latest_release_for_package(package_name: str) -> Optional[Release]:
        return Release("1.2.0", datetime.datetime.now())
        



