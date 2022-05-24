from pydantic import BaseModel as PyModel, EmailStr, validator, Extra

from app.models import StoreInSessionMixin


class Login(PyModel):
    email: EmailStr
    password: str

    class Config:
        extra = Extra.ignore


class Auth(StoreInSessionMixin, PyModel):
    access_token: str
    refresh_token: str


class RegisterUser(PyModel):
    email: EmailStr
    password: str
    password_submit: str

    class Config:
        extra = Extra.ignore

    @validator('password_submit')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('passwords do not match')
        return v
