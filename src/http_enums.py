from enum import Enum


class HttpMethods(str, Enum):
    PUT = "PUT"
    GET = "GET"
    POST = "POST"
    PATCH = "PATCH"


class HttpStatuses(int, Enum):
    OK = 200
    CREATED = 201
    FORBIDDEN = 403
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    INTERNAL_SERVER_ERROR = 500
