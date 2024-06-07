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
async def get_recipes(db: Session = Depends(get_db)):
    return db.query(models.Recipe).all()

@router.get("/search/{ingr}",response_model=List[pyd.RecipeScheme])
async def search_by_ingr(ingr:str,db: Session = Depends(get_db)):
    ingr_db=db.query(models.Ingredient).filter(models.Ingredient.name==ingr).first()
    if not ingr_db:
        raise HTTPException(status_code=404, detail="Ингредиент не найден!")
    recipe_db=db.query(models.Count).filter(models.Count.id_ingredient==ingr_db.id).all()
    if recipe_db ==[]:
        raise HTTPException(status_code=404, detail="Нет рецепта")
    arr=[]
    for i in recipe_db:
        rec = db.query(models.Recipe).filter(models.Recipe.id==i.id_recipe).first()
        arr.append(rec)
    return arr

@router.get("/search_name/{name}",response_model=List[pyd.RecipeScheme])
async def search_by_name(name:str,db: Session = Depends(get_db)):
    rec_db=db.query(models.Recipe).filter(models.Recipe.name==name).all()
    if not rec_db:
        raise HTTPException(status_code=404, detail="Рецепт не найден!")
    return rec_db

@router.post('/')
async def create_recipes(recipe_input:pyd.RecipeCreate,count_input:List[pyd.CountCreate],db:Session=Depends(get_db), username=Depends(auth_handler.auth_wrapper)):
    recipe_db=models.Recipe()
    recipe_db.name=recipe_input.name
    recipe_db.cooking_time=recipe_input.cooking_time
    recipe_db.info=recipe_input.info
    err = False
    det = ""
    for count_int in count_input:
        count_db=models.Count()
        count_db.recipe=recipe_db
        ing_db=db.query(models.Ingredient).filter(models.Ingredient.id==count_int.id_ingredient).first() 
        if not ing_db:
            err = True
            det="Ингредиент не найден!"
            break
        count_db.id_ingredient=ing_db.id
        count_db.count=count_int.count
        sys_db=db.query(models.System_of_calculation).filter(models.System_of_calculation.id==count_int.id_system_of_calc).first() 
        if not sys_db:
            err = True
            det = "Система исчисления не найдена!"
            break
        count_db.id_system_of_calc = sys_db.id
        ingr_pov=db.query(models.Count).filter(models.Count.id_recipe==recipe_db.id).filter(models.Count.id_ingredient==count_int.id_ingredient).first()
        if ingr_pov:
            err = True
            det = "Ингредиент дублируется"
            break
        if not ingr_pov and ing_db and sys_db:
            db.add(count_db)
            db.commit()
    if err == True:
        raise HTTPException(404, detail=det)
    db.add(recipe_db)
    db.commit()
    return "Рецепт добавлен"

@router.put('/{recipe_id}')
async def update_recipes(recipe_id:int,recipe_input:pyd.RecipeCreate,count_input:List[pyd.CountCreate],db:Session=Depends(get_db), username=Depends(auth_handler.auth_wrapper)):
    recipe_db=db.query(models.Recipe).filter(models.Recipe.id==recipe_id).first()
    recipe_db.name=recipe_input.name
    recipe_db.cooking_time=recipe_input.cooking_time
    recipe_db.info=recipe_input.info
    err = False
    det = ""
    db.query(models.Count).filter(models.Count.id_recipe==recipe_id).delete()
    for count_int in count_input:
        count_db=models.Count()
        count_db.recipe=recipe_db
        ing_db=db.query(models.Ingredient).filter(models.Ingredient.id==count_int.id_ingredient).first() 
        if not ing_db:
            err = True
            det="Ингредиент не найден!"
            break
        count_db.id_ingredient=ing_db.id
        count_db.count=count_int.count
        sys_db=db.query(models.System_of_calculation).filter(models.System_of_calculation.id==count_int.id_system_of_calc).first() 
        if not sys_db:
            err = True
            det = "Система исчисления не найдена!"
            break
        count_db.id_system_of_calc = sys_db.id
        if ing_db and sys_db:
            db.add(count_db)
            db.commit()
    if err == True:
        raise HTTPException(404, detail=det)
    db.add(recipe_db)
    db.commit()
    return "Рецепт изменен"

@router.delete('/{recipe_id}')
async def delete_recipe(recipe_id:int, db:Session=Depends(get_db),username=Depends(auth_handler.auth_wrapper)):
    recipe_db=db.query(models.Recipe).filter(models.Recipe.id==recipe_id).first()
    if not recipe_id:
        raise HTTPException(status_code=404, detail="Рецепт не найден")
    db.query(models.Count).filter(models.Count.id_recipe==recipe_id).delete()
    db.delete(recipe_db)
    db.commit()
    return "Удаление рецепта прошло успешно"