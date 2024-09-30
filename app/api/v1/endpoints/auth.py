from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from core.security import create_access_token
from core.database import get_session
from services.user_service import authenticate_user, register_user
from schemas.user_schema import UserCreate, UserAuth
from schemas.token_schema import TokenResponse
from app.helpers.exception_handler import CustomException

router = APIRouter()

@router.post("/sign-in", response_model = TokenResponse)
def login(user_data: UserAuth, session: Session = Depends(get_session)):
    user = authenticate_user(session, user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Invalid credentials")
    
    access_token = create_access_token(data = {"sub": user.email})
    return TokenResponse(access_token = access_token, token_type="bearer")

@router.post("/sign-up")
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    try:
        return register_user(session, user_data)
    except Exception as e:
        raise CustomException(http_code = status.HTTP_400_BAD_REQUEST, message = str(e))
