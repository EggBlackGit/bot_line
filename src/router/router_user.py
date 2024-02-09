
from fastapi import APIRouter
import src.models.model_users as models

users = APIRouter()

@users.get("/")
def get_users():
    return {"eee":"111"}

@users.post("/create-user")
def create_user(create_user: models.Create_user_model) -> models.Create_user_model:
    return create_user