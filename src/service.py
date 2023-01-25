from typing import Any, Callable
from datetime import datetime, timedelta, timezone

from flask import Flask, request, Request, Response, make_response

from flask_mysqldb import MySQL
from jwt.exceptions import PyJWTError

from src.http_enums import HttpStatuses
from src.utils import create_jwt, decode_jwt
from src.settings import settings


class AuthService:
    @staticmethod
    def login(request: Request, sql_cursor: Callable[[], [Any]]) -> Response:

        if not request.authorization:
            return make_response(
                {"message": "Missing auth credentials"},
                HttpStatuses.BAD_REQUEST.value,
            )

        email = request.authorization.username.strip()
        password = request.authorization.password.strip()

        if not all((email, password)):
            return make_response(
                {"message": "email and password fields are required"},
                HttpStatuses.BAD_REQUEST.value,
            )

        cursor = sql_cursor()
        result = cursor.execute(
            "SELECT id, email, password FROM user WHERE email=%s", (email,)
        )

        if result == 0:
            return make_response(
                {"message": "invalid sign in credentials"},
                HttpStatuses.UNAUTHORIZED.value,
            )

        user_id, user_email, user_password = cursor.fetchone()

        if password != user_password:
            return make_response(
                {"message": "invalid sign in credentials"},
                HttpStatuses.UNAUTHORIZED.value,
            )

        encoded_jwt = create_jwt(user_id, user_email, is_admin=False)
        return make_response({"data": encoded_jwt}, HttpStatuses.OK.value)

    @staticmethod
    def validate_jwt(request: Request) -> Response:
        authorization = request.headers.get("Authorization")
        if not authorization:
            return make_response(
                {"message": "Missing authorization"}, HttpStatuses.BAD_REQUEST.value
            )

        try:
            bearer, token = authorization.split(" ")

            if bearer != "Bearer":
                raise IndexError()
            decoded_jwt = decode_jwt(token)
        except IndexError:
            return make_response(
                {
                    "message": "Authorization header must be in the format: 'Bearer <Token>'"
                },
                HttpStatuses.BAD_REQUEST.value,
            )
        except PyJWTError as E:
            return make_response({"message": E.__str__()}, HttpStatuses.UNAUTHORIZED.value)
        except Exception:
            return make_response(
                {"message": "Unauthorized"},
                HttpStatuses.UNAUTHORIZED.value,
            )
        else:
            return make_response({"data": decoded_jwt}, HttpStatuses.OK.value)
