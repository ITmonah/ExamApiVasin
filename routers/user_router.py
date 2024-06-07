from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
from auth import AuthHandler

# контролер пользователя
router = APIRouter(
    prefix="/user",
    tags=["user"],
)

auth_handler = AuthHandler()

def get_current_auth_user(payload:dict=Depends(auth_handler.auth_wrapper), db:Session=Depends(get_db)):
    username:str | None = payload
    users_db=db.query(models.User).filter(models.User.name==username).first()
    if users_db:
        return users_db
    raise HTTPException(status_code=401, detail="Токен не найден")

# регистрация
@router.post("/register", response_model=pyd.UserBase)
async def register_user(user_input: pyd.UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(models.User.name == user_input.name).first()
    user_mail_db = db.query(models.User).filter(models.User.mail == user_input.mail).first()
    if user_db:
        raise HTTPException(400, 'Имя занято')
    if user_mail_db:
        raise HTTPException(400, 'Почта занята')
    hash_pass = auth_handler.get_password_hash(user_input.password)
    user_db = models.User(
        name=user_input.name,
        password=hash_pass,
        mail = user_input.mail
    )
    db.add(user_db)
    db.commit()
    return user_db

# авторизация и выдача JWT токена
@router.post('/login')
async def user_login(user_input: pyd.UserLog, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.name == user_input.name
    ).first()
    if not user_db:
        raise HTTPException(404, 'Логин не найден')

    if auth_handler.verify_password(user_input.password, user_db.password):
        token = auth_handler.encode_token(user_db.name)
        return {'token': token}
    else:
        raise HTTPException(403, 'Пароль не верен')
    
@router.get('/all')
async def get_users(db:Session=Depends(get_db)):
    users_db=db.query(models.User).all()
    return users_db

@router.get("/me")
def auth_user_check_self_info(payload:dict=Depends(auth_handler.auth_wrapper), user:pyd.UserBase=Depends(get_current_auth_user)):
    return {
        "username": user.name,
        "email": user.mail,
        }