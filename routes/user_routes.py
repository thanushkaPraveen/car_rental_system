from fastapi import APIRouter

from services.auth_service import AuthService

router = APIRouter()
controller = AuthService()

@router.post("/login")
def login(user: dict):
    return controller.login(user["email"], user["password"])

@router.post("/register")
def register(user: dict):
    return controller.register(user)