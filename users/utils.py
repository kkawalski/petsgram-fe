from typing import List

from pydantic import parse_obj_as

from app import Config
from app.utils import check_response_errors
from auth.utils import request_with_auth
from users.models import Avatar, Profile, UploadFile #, MyProfile


PROFILES_URL = f"{Config.API_URL}/profiles/"
MY_PROFILE_URL = f"{Config.API_URL}/profiles/my-profile"
AVATAR_URL = f"{Config.API_URL}/images/avatar"


def create_profile(*args, **kwargs) -> Profile:
    pre_profile = Profile(**kwargs)
    res = request_with_auth("POST", PROFILES_URL, json=pre_profile.dict_without_none())
    check_response_errors(res, 201)
    profile = Profile(**res.json())
    return profile


def get_my_profile() -> Profile:
    res = request_with_auth("GET", MY_PROFILE_URL)
    check_response_errors(res, 200)
    # valid_profile = MyProfile(**res.json())
    # profile = Profile(**valid_profile.dict_without_none(exclude="user"))
    profile = Profile(**res.json())
    return profile


def update_my_profile(*args, **kwargs) -> Profile:
    pre_profile = Profile(**kwargs)
    res = request_with_auth("PUT", MY_PROFILE_URL, json=pre_profile.dict_without_none())
    check_response_errors(res, 202)
    # valid_profile = MyProfile(**res.json())
    # profile = Profile(**valid_profile.dict_without_none(exclude={"user"}))
    profile = Profile(**res.json())
    return profile


def upload_avatar(*args, **kwargs) -> Avatar:
    pre_avatar = UploadFile(**kwargs)
    res = request_with_auth("POST", AVATAR_URL, files={"file": (pre_avatar.file.filename, pre_avatar.file.read())})
    check_response_errors(res, 201)
    avatar = Avatar(**res.json())
    return avatar


def get_profiles(*args, **kwargs) -> List[Profile]:
    res = request_with_auth("GET", PROFILES_URL)
    check_response_errors(res, 200)
    profiles = parse_obj_as(List[Profile], res.json())
    return profiles
