from typing import Optional
from pydantic import BaseModel, conint


class UserRegister(BaseModel):
    pass


class UserLogin(BaseModel):
    """

    """
    username: str
    password: str


class TokenPayload(BaseModel):
    sub: Optional[int] = None
