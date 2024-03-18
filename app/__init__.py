from fastapi import FastAPI

from app.setting.connection import Base, engine
from app.models.user import User, Repayment

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Repayment")

@app.get("/")
def home():
    User()
    Repayment
    pass
