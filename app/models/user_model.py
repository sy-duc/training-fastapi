from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table = True):
    __tablename__ = "users"  # Table name in database
        
    id: Optional[int] = Field(default = None, primary_key = True)
    full_name: str
    email: str
    password: str
    role: Optional[str] = Field(default = 'user')
