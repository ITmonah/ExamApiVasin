from fastapi import FastAPI
import models
from database import SessionLocal, engine
from routers import user_router, recipe_router

# Инициализация фастапи
app = FastAPI()

# подключение АпиРоутера (маршруты сущности)
app.include_router(user_router)
app.include_router(recipe_router)
