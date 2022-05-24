from flask import abort
import requests

from werkzeug.exceptions import HTTPException

from app.models import ErrorModel


def check_response_errors(response: requests.Response, success_code: int = 200) -> None:
    if response.status_code != success_code:
        error = ErrorModel(**response.json())
        abort(response.status_code, error.message)
