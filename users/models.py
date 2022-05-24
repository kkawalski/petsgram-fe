from typing import Optional

from pydantic import EmailStr, HttpUrl

from app.models import BaseModel, StoreInSessionMixin


class User(StoreInSessionMixin, BaseModel):
    email: EmailStr
    is_active: bool = True
    is_admin: bool = False
    has_profile: bool = False


class Avatar(BaseModel):
    filename: str
    url: HttpUrl
    object_id: int
    object_type: str


class Profile(StoreInSessionMixin, BaseModel):
    first_name: str
    last_name: str
    description: Optional[str]
    avatar: Optional[Avatar]


class MyProfile(Profile):
    user: User
