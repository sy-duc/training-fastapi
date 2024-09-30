from sqlmodel import Session, select
from models.user_model import User
from schemas.user_schema import UserUpdate

def create_user(session: Session, user: User) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session) -> list[User]:
    statement = select(User)
    return session.exec(statement).all()

def get_user_by_email(session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def update_user(session: Session, user_id: int, user_data: UserUpdate) -> User | None:
    user = session.get(User, user_id)
    if user:
        user.full_name = user_data.full_name
        session.commit()
        session.refresh(user)
        return user
    return None

def delete_user(session: Session, user_id: int) -> bool:
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False
