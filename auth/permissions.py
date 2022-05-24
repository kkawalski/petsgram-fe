from functools import wraps

from flask import abort

from app.errors import NEED_PROFILE
from auth.models import Auth
from auth.utils import get_current_user
from users.models import User


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = User.from_session()
        if user is None:
            auth = Auth.from_session()
            if auth is None:
                abort(401)
            user = get_current_user()
            user.store_in_session()
        return func(*args, **kwargs)
    return wrapper


def profile_required(func):
    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):
        user = User.from_session()
        if not user.has_profile:
            abort(403, NEED_PROFILE)
        return func(*args, **kwargs)
    return wrapper
