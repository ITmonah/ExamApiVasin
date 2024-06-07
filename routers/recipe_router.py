from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
from auth import AuthHandler

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
)

auth_handler = AuthHandler()

@router.get("/", response_model=List[pyd.RecipeScheme])
async def get_products(db: Session = Depends(get_db)):
    return db.query(models.Recipe).all()