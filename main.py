from fastapi import FastAPI
from auth_rutas import router
from user_api import router as user_router

app = FastAPI()

app.include_router(router, prefix="/auth")
app.include_router(user_router)