from datetime import datetime
from typing import Optional

from flask import session

from pydantic import BaseModel as PyModel


class BaseModel(PyModel):
    id: Optional[int]
    created: Optional[datetime]
    modified: datetime = None

    def dict_without_none(self, **kwargs):
        return self.dict(exclude_none=True, **kwargs)


class StoreInSessionMixin:
    def store_in_session(self: BaseModel, **kwargs):
        session[self.__class__.__name__.lower()] = self.dict()
        session.modified = True

    @classmethod
    def from_session(cls):
        data = session.get(cls.__name__.lower())
        if data is not None:
            return cls(**data)


class ErrorModel(PyModel):
    message: str = "Something Wrong."
