# app/main.py
from fastapi import FastAPI # pyright: ignore[reportMissingImports]

app = FastAPI(
    title="Risk Dashboard API",
    description="API for US stock portfolio risk metrics",
    version="0.1.0"
)

from app.api.routes import router

app.include_router(router)