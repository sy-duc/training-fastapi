from fastapi import APIRouter, Depends, status, HTTPException
from sqlmodel import Session

from dependencies import get_current_user, PermissionRequired
from core.database import get_session
from services.user_service import read_users, edit_user
from schemas.user_schema import UserUpdate, UserResponse
from models.user_model import User
from app.helpers.exception_handler import CustomException

router = APIRouter(
    # dependencies = [Depends(get_current_user)] # If all the endpoints in this route require authentication
)

@router.get("/", dependencies = [Depends(get_current_user)], response_model = list[UserResponse])
def get(session: Session = Depends(get_session)):
    users = read_users(session)
    return users

@router.put("/{user_id}", dependencies = [Depends(PermissionRequired('admin'))], response_model = UserResponse)
def update(
    user_id: int,
    user_data: UserUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    try:
        if current_user.id != user_id:
            raise HTTPException(
                status_code = status.HTTP_403_FORBIDDEN,
                detail = "You do not have permission to update this user"
            )
        user_updated = edit_user(session, user_id, user_data)
        return user_updated
    except Exception as e:
        raise CustomException(http_code = status.HTTP_400_BAD_REQUEST, message = str(e))
