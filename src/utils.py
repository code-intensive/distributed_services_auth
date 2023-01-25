from datetime import datetime, timedelta
from typing import Dict, Any

import jwt

from src.settings import settings
import src.utils


def create_jwt(user_id: str, email: str, is_admin: bool = False) -> str:
    return jwt.encode(
        {
            "sub": user_id,
            "email": email,
            "is_admin": is_admin,
            "exp": datetime.utcnow() + timedelta(days=1),
            "iat": datetime.utcnow(),
        },
        key=settings.JWT_SECRET,
        algorithm=settings.HASH_ALGORITHM,
    )


def decode_jwt(jwt_token: str) -> Dict[str, Any]:
    return jwt.decode(
        jwt_token,
        key=settings.JWT_SECRET,
        verify=True,
        algorithms=[settings.HASH_ALGORITHM],
    )
