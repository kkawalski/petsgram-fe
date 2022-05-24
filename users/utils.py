from pickle import GET
from app import Config
from app.utils import check_response_errors
from auth.utils import request_with_auth
from users.models import MyProfile, Profile


PROFILES_URL = f"{Config.API_URL}/profiles/"
MY_PROFILE_URL = f"{Config.API_URL}/profiles/my-profile"


def create_profile(*args, **kwargs) -> Profile:
    pre_profile = Profile(**kwargs)
    print("PRE PROFILE", pre_profile)
    res = request_with_auth("POST", PROFILES_URL, json=pre_profile.dict_without_none())
    print("RES", res)
    check_response_errors(res, 201)
    profile = Profile(**res.json())
    return profile


def get_my_profile() -> Profile:
    res = request_with_auth("GET", MY_PROFILE_URL)
    check_response_errors(res, 200)
    valid_profile = MyProfile(**res.json())
    profile = Profile(**valid_profile.dict_without_none(exclude="user"))
    return profile


def update_my_profile(*args, **kwargs) -> Profile:
    pre_profile = Profile(**kwargs)
    res = request_with_auth("PUT", MY_PROFILE_URL, json=pre_profile.dict_without_none())
    check_response_errors(res, 202)
    valid_profile = MyProfile(**res.json())
    profile = Profile(**valid_profile.dict_without_none(exclude="user"))
    return profile
