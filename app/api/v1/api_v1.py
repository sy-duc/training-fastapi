from fastapi import APIRouter
from api.v1.endpoints import auth, users

api_router = APIRouter()

# Register the route from the module
api_router.include_router(auth.router, prefix = "/auth", tags = ["auth"])
api_router.include_router(users.router, prefix = "/users", tags = ["users"])
