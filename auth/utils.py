from flask import session
import requests

from app import Config
from app.utils import check_response_errors
from auth.models import Login, Auth, RegisterUser
from users.models import User


LOGIN_URL = f"{Config.API_URL}/auth/login"
REFRESH_URL = f"{Config.API_URL}/auth/refresh"
CURRENT_USER_URL = f"{Config.API_URL}/auth/me"
CREATE_USER_URL = f"{Config.API_URL}/auth/"


def access(*args, **kwargs) -> Auth:
    login = Login(**kwargs)
    res = requests.post(LOGIN_URL, json=login.dict())
    check_response_errors(res, 200)
    auth = Auth(**res.json())
    return auth


def refresh() -> Auth:
    auth = Auth.from_session()
    res = requests.post(REFRESH_URL, headers={
        "Authorization": f"Bearer {auth.refresh_token}"
    })
    check_response_errors(res, 200)
    auth.access_token = res.json()["access_token"]
    return auth


def request_with_auth(
    method: str = None, url: str = None,
    headers: dict = None, files: dict = None,
    data: dict = None, json: dict = None,
    **kwargs,
) -> requests.Response:
    if headers is None:
        headers = {}

    auth_data = kwargs.get("auth") or session.get("auth")
    auth = Auth(**auth_data)

    headers.update(Authorization=f"Bearer {auth.access_token}")

    req = requests.Request(
        method=method, url=url,
        headers=headers, files=files,
        data=data, json=json,
        **kwargs
    )
    r = req.prepare()
    s = requests.Session()
    return s.send(r)


def get_current_user() -> User:
    res = request_with_auth("GET", CURRENT_USER_URL)
    check_response_errors(res, 200)
    user = User(**res.json())
    return user


def create_user(*args, **kwargs) -> User:
    register_user = RegisterUser(**kwargs)
    res = requests.post(CREATE_USER_URL, json=register_user.dict())
    check_response_errors(res, 201)
    user = User(**res.json())
    return user
