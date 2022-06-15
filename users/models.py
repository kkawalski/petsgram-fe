from typing import Optional, Union

from werkzeug.datastructures import FileStorage
from pydantic import EmailStr, Extra, HttpUrl, validator

from app.models import BaseModel, StoreInSessionMixin


class User(StoreInSessionMixin, BaseModel):
    email: EmailStr
    is_active: bool = True
    is_admin: bool = False
    has_profile: bool = False


class UploadFile(BaseModel):
    file: FileStorage

    class Config:
        arbitrary_types_allowed = True


class Avatar(BaseModel):
    filename: str
    url: HttpUrl
    # object_id: int
    # object_type: str


class Profile(StoreInSessionMixin, BaseModel):
    first_name: str
    last_name: str
    description: Optional[str]
    avatar: Optional[Avatar]

    class Config:
        extra = Extra.ignore

# class MyProfile(Profile):
#     user: User
