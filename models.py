from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, DateTime, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType, URLType
from sqlalchemy.sql import func

from database import Base

class User(Base): #пользователи
    __tablename__ = "users"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False, unique=True)
    mail = Column(EmailType, nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())

class Recipe(Base): #рецепты
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True) 
    name = Column(String(255), nullable=False)
    face_img = Column(String(255), nullable=False, default="http://127.0.0.1:8000/recipe/files/food.png") #фото обязательно
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())
    cooking_time=Column(Integer, nullable=False)

    counts: Mapped[list["Count"]] = relationship(
        primaryjoin="and_(Recipe.id == Count.id_recipe)"
        )

class Ingredient(Base): #ингредиенты
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

class System_of_calculation(Base): #система исчисления
    __tablename__ = "system_of_calculations"

    id = Column(Integer, primary_key=True) 
    name = Column(String(255), nullable=False)

class Count(Base): #таблица, связывающая ингредиенты и рецепты
    __tablename__ = "counts"

    id = Column(Integer, primary_key=True)
    id_recipe = Column(Integer, ForeignKey('recipes.id'), nullable=False, default=1)
    id_ingredient = Column(Integer, ForeignKey('ingredients.id'), nullable=False, default=1)
    count = Column(Integer, nullable=False, default=1)
    id_system_of_calc = Column(Integer, ForeignKey('system_of_calculations.id'), nullable=False, default=1)

    recipe: Mapped["Recipe"] = relationship(back_populates='counts')
    ingredient: Mapped["Ingredient"] = relationship(backref='counts')
    system_of_calc: Mapped["System_of_calculation"] = relationship( backref='counts') #система исчисления
