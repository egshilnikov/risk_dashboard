# src/main.py
from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from api.routes import router
from models.database import Base, engine # pyright: ignore[reportMissingImports]
import models.portfolio  # import all model files

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Risk Dashboard API",
    description="API for US stock portfolio risk metrics",
    version="0.1.0"
)
app.include_router(router)