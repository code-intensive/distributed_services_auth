__all__ = ("settings",)

from os import getenv
from typing import Dict, Any, Union

from dotenv import load_dotenv

load_dotenv()


class Settings:

    __API_VERSION = "v1"
    __HASH_ALGORITHM = "HS256"

    __MYSQL_COFIG = {
        "MYSQL_DB": getenv("MYSQL_DB"),
        "MYSQL_HOST": getenv("MYSQL_HOST"),
        "MYSQL_PORT": int(getenv("MYSQL_PORT")),
        "MYSQL_USER": getenv("MYSQL_USER"),
        "MYSQL_PASSWORD": getenv("MYSQL_PASSWORD"),
    }

    __JWT_SECRET = getenv("JWT_SECRET")

    @property
    def API_VERSION(self) -> str:
        return self.__API_VERSION

    @property
    def MYSQL_COFIG(self) -> Dict[str, Union[str, int]]:
        return self.__MYSQL_COFIG

    @property
    def JWT_SECRET(self) -> str:
        return self.__JWT_SECRET

    @property
    def HASH_ALGORITHM(self) -> str:
        return self.__HASH_ALGORITHM


settings = Settings()
