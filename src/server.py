from datetime import datetime, timedelta, timezone

import jwt
from flask import Flask, request, Request, Response

from flask_mysqldb import MySQL

from src.service import AuthService
from src.settings import settings
from src.http_enums import HttpMethods


server = Flask(__name__)
mysql = MySQL(server)

server.config.update(settings.MYSQL_COFIG)


@server.route(f"/api/{settings.API_VERSION}/auth/sign-in", methods=[HttpMethods.POST])
def login() -> Response:
    return AuthService.login(request, mysql.connection.cursor)


@server.route(
    f"/api/{settings.API_VERSION}/auth/validate-jwt", methods=[HttpMethods.POST]
)
def validate_jwt() -> Response:
    return AuthService.validate_jwt(request)
