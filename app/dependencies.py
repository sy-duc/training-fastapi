import logging
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt.exceptions import InvalidTokenError
from pydantic import ValidationError
from sqlmodel import Session
from typing import Annotated

from core.database import get_session
from schemas.token_schema import TokenPayload
from core.config import settings
from crud.user import get_user_by_email
from models.user_model import User

logger = logging.getLogger()
reusable_oauth2 = HTTPBearer(scheme_name = "Authorization")

def get_current_user(http_authorization_credentials: Annotated[HTTPAuthorizationCredentials, Depends(reusable_oauth2)], session: Annotated[Session, Depends(get_session)]):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate": "Bearer"}
    )
    try:
        logger.info(http_authorization_credentials.credentials)
        token =  http_authorization_credentials.credentials
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms = [settings.ALGORITHM])
        token_data = TokenPayload(**payload)
        logger.info(token_data)
    except (InvalidTokenError, ValidationError):
        raise credentials_exception
    
    user = get_user_by_email(session, token_data.sub)
    if user is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    return user

class PermissionRequired:
    def __init__(self, *args):
        self.user = None
        self.permissions = args

    def __call__(self, user: User = Depends(get_current_user)):
        self.user = user
        if self.user.role not in self.permissions and self.permissions:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail = f'User {self.user.email} can not access this api'
            )
