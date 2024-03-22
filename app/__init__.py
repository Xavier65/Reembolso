from fastapi import FastAPI

from app.routers import user, repayment, repayment_detail
from app.setting.connection import Base, engine

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

server = FastAPI(title="Repayment")

server.include_router(user.router)
server.include_router(repayment.router)
server.include_router(repayment_detail.router)
