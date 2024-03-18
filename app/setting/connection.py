from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from  decouple import config

DATABASE:str = config('DATABASE_URL')
engine = create_engine(DATABASE, echo=False)
lsession = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = lsession()
    try:
        yield db
    finally:
        db.close()

