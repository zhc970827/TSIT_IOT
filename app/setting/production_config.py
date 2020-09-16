import os

from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    
    DOCS_URL: Optional[str] = "/api/v1/docs"
    
    OPENAPI_URL: Optional[str] = "/api/v1/openapi.json"
    
    REDOC_URL: Optional[str] = None
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = '-*&^)()sd(*A%&^aWEQaasda_asdasd*&*)(asd%$#'

    POSTGRESQL_USERNAME: str = os.getenv("POSTGRESQL_USER", "postgres")
    POSTGRESQL_PASSWORD: str = os.getenv("POSTGRESQL_PASSWORD", "postgres")
    POSTGRESQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = os.getenv("POSTGRESQL_HOST", "127.0.0.1")
    POSTGRESQL_DATABASE: str = ''

    SQLALCHEMY_DATABASE_URI = f"POSTGRESQL+pyPOSTGRESQL://{POSTGRESQL_USERNAME}:{POSTGRESQL_PASSWORD}@" \
                              f"{POSTGRESQL_HOST}/{POSTGRESQL_DATABASE}?charset=utf8mb4"


config = Config()