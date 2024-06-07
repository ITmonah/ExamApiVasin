from datetime import date, datetime
from pydantic import EmailStr, BaseModel, Field, FileUrl 

class UserBase(BaseModel):
    id:int=Field(...,gt=0,example=2) #обязательно к заполнению
    name:str=Field(...,example="Gena")
    mail:EmailStr = Field(...,example="gena228@mail.ru")
    created_at:datetime=Field(...,example='2024-01-01 00:00:00')
    class Config:
        orm_mode=True #наша модель будет легко соедняться с бд

class RecipeBase(BaseModel):
    id:int=Field(...,gt=0,example=22) 
    name:str=Field(...,example="Мясной пирог")
    info:str=Field(...,max_length=1000, min_length=1,example="Заверните сосиску в тесто и выпекайте 20 минут в духовке")
    created_at:datetime=Field(...,example='2024-01-01 00:00:00')
    cooking_time:int=Field(..., gt=0, example=30)
    class Config:
        orm_mode=True 

class IngredientBase(BaseModel):
    id:int=Field(...,gt=0,example=2)
    name:str=Field(...,example="Яйцо")
    class Config:
        orm_mode=True

class System_of_calculationBase(BaseModel):
    id:int=Field(...,gt=0,example=3) 
    name:str=Field(...,example="кг")
    class Config:
        orm_mode=True 

class CountBase(BaseModel): #таблица, связывающая ингредиенты и рецепты
    id:int=Field(...,gt=0,example=3) 
    count:int=Field(...,gt=0,example=10)
    class Config:
            orm_mode=True 
