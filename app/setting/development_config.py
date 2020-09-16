from typing import Union, Optional
from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    # 
    DOCS_URL: str = "/api/v1/docs"
    #
    OPENAPI_URL: str = "/api/v1/openapi.json"
    #
    REDOC_URL: Optional[str] = None
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 *8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    POSTGRESQL_USERNAME: str = ''
    POSTGRESQL_PASSWORD: str = ""
    POSTGRESQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = ""
    POSTGRESQL_DATABASE: str = ''

    # 
    SQLALCHEMY_DATABASE_URI = f"POSTGRESQL+pyPOSTGRESQL://{POSTGRESQL_USERNAME}:{POSTGRESQL_PASSWORD}@" \
                              f"{POSTGRESQL_HOST}/{POSTGRESQL_DATABASE}?charset=utf8mb4"


config = Config()