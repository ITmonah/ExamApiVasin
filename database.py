from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" #строка подключения

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

def get_db(): 
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    def __repr__(self):
        cols=[]
        for col in self.__table__.columns.keys():
            cols.append(f"{col}={getattr(self,col)}")
        return f"<{self.__class__.__name__} {','.join(cols)}>"