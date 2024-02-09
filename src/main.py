import src.setting as stg

from fastapi import FastAPI
from src.router import (users, linebot)

app = FastAPI(
    docs_url="/docs" if stg.IS_DEBUG else None,
    redoc_url="/redoc" if stg.IS_DEBUG else None,
)

@app.get("/")
def health_check():
    return {"health": "200"}

app.include_router(users, prefix="/users", tags=["Users"])
app.include_router(linebot, prefix="/linebot", tags=["Linebot"])
