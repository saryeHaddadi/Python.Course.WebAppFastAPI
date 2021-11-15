import datetime


class User:
    def __init__(self, name: str, email: str, hash_password: str):
        self.id = 1
        self.name = name
        self.email = email
        hash_password = hash_password
        self.created_date = None
        self.profile_image_url = ""
        self.last_login: datetime.datetime = None







