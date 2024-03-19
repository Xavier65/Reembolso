from fastapi import FastAPI

from app.routers import user, repayment
from app.setting.connection import Base, engine

#Base.metadata.drop_all(bind=engine)
#Base.metadata.create_all(bind=engine)

app = FastAPI(title="Repayment")

app.include_router(user.router)
app.include_router(repayment.router)