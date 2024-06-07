from pydantic import EmailStr,BaseModel, Field, FileUrl #какой формат данных хотим от пользователя
from typing import List, Dict

class UserCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Gena")
    mail:EmailStr = Field(...,example="gena228@mail.ru")
    password:str=Field(...,max_length=255, min_length=4,example="1235")

class UserLog(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Gena")
    password:str=Field(...,max_length=255, min_length=4,example="1235")

class RecipeCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Сосиска в тесте")
    info:str=Field(...,max_length=1000, min_length=1,example="Заверните сосиску в тесто и выпекайте 20 минут в духовке")
    cooking_time:int=Field(..., gt=0, example=2) #время готовки

class IngredientCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="Морковка")

class System_of_calculationCreate(BaseModel):
    name:str=Field(...,max_length=255, min_length=1,example="кг")

class CountCreate(BaseModel):
    id_ingredient:int=Field(..., gt=0, example=10)
    count:int=Field(..., gt=0, example=10)
    id_system_of_calc:int=Field(..., gt=0, example=10)