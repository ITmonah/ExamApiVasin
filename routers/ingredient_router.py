from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
from auth import AuthHandler

router = APIRouter(
    prefix="/ingredient",
    tags=["ingredient"],
)

auth_handler = AuthHandler()

@router.get('/', response_model=List[pyd.IngredientBase])
async def get_ingredients(db:Session=Depends(get_db)):
    ingredients=db.query(models.Ingredient).all()
    return ingredients

@router.post('/', response_model=pyd.IngredientBase)
async def create_ingredients(ingredient_input:pyd.IngredientCreate, db:Session=Depends(get_db),username=Depends(auth_handler.auth_wrapper)):
    ingredient_db=db.query(models.Ingredient).filter(models.Ingredient.name==ingredient_input.name).first()
    if ingredient_db:
        raise HTTPException(400, 'Ингредиент уже есть')
    ingredient_db=models.Ingredient()
    ingredient_db.name=ingredient_input.name
    db.add(ingredient_db)
    db.commit()
    return ingredient_db

@router.put('/{ingredient_id}', response_model=pyd.IngredientBase)
async def update_ingredients(ingredient_id:int, ingredient_input:pyd.IngredientCreate, db:Session=Depends(get_db),username=Depends(auth_handler.auth_wrapper)):
    ingredient_db=db.query(models.Ingredient).filter(models.Ingredient.id==ingredient_id).first()
    if not ingredient_db:
        raise HTTPException(status_code=404, detail="Ингредиент не найден")
    ingredient_db1=db.query(models.Ingredient).filter(models.Ingredient.name==ingredient_input.name).first()
    if ingredient_db1:
        raise HTTPException(400, 'Ингредиент уже есть')
    ingredient_db.name=ingredient_input.name
    db.commit()
    return ingredient_db

@router.delete('/{ingredient_id}')
async def delete_ingredients(ingredient_id:int, db:Session=Depends(get_db),username=Depends(auth_handler.auth_wrapper)):
    ingredient_db=db.query(models.Ingredient).filter(models.Ingredient.id==ingredient_id).first()
    if not ingredient_db:
        raise HTTPException(status_code=404, detail="Ингредиент не найден")
    db.query(models.Count).filter(models.Count.id_ingredient==ingredient_id).delete()
    db.delete(ingredient_db)
    db.commit()
    return "Удаление ингредиента прошло успешно"