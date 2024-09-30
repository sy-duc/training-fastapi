import jwt
from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from core.config import settings

# Hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS
    )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt

# Verify password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Create a hash for the password
def get_password_hash(password: str):
    return pwd_context.hash(password)
