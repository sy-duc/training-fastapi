from sqlmodel import Session
from fastapi import status, HTTPException

from crud.user import get_users, get_user_by_email, create_user, update_user, delete_user
from schemas.user_schema import UserAuth, UserResponse, UserCreate, UserUpdate
from core.security import verify_password, get_password_hash
from models.user_model import User

def read_users(session: Session) -> list[UserResponse]:
    users = get_users(session)
    return [UserResponse(**user.model_dump()) for user in users]

def authenticate_user(session: Session, email: str, password: str) -> UserAuth | None:
    user = get_user_by_email(session, email)
    if user and verify_password(password, user.password):
        return user
    return None

def register_user(session: Session, user: UserCreate) -> UserResponse:
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password  # Update the password to hashed version
    user_created = create_user(session, User(**user.model_dump()))
    return UserResponse(**user_created.model_dump())

def edit_user(session: Session, user_id: int, user_data: UserUpdate) -> UserResponse | None:
    user_updated = update_user(session, user_id, user_data)
    if user_updated is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    return UserResponse(**user_updated.model_dump())

def delete_user(session: Session, user_id: int) -> bool:
    return delete_user(session, user_id)
