import datetime
import sqlalchemy as sa
from app.models.base.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name: str = sa.Column(sa.String)
    email: str = sa.Column(sa.String, index=True, unique=True)
    hash_password: str = sa.Column(sa.String)
    created_date: datetime.datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    last_login: datetime.datetime = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    profile_image_url: str = sa.Column(sa.String)

