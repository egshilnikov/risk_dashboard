# app/api/routes.py
from fastapi import APIRouter # pyright: ignore[reportMissingImports]
from models.portfolio import PortfolioInput, PortfolioResult # pyright: ignore[reportMissingImports]

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/portfolio", response_model=PortfolioResult)
def calculate_risk(data: PortfolioInput):
    # Mock response for now
    return PortfolioResult(
        portfolio_name=data.portfolio_name,
        var_95=1200.00,
        var_99=1600.00,
        stress_loss=2000.00
    )

@router.get("/")
def read_root():
    return {"message": "Welcome to the Risk Dashboard API"}