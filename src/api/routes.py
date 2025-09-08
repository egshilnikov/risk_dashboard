# src/api/routes.py
from fastapi import APIRouter # pyright: ignore[reportMissingImports]
from fastapi.responses import Response # pyright: ignore[reportMissingImports]
from models.portfolio import PortfolioInput, PortfolioResult # pyright: ignore[reportMissingImports]
from tasks.worker import calculate_var
import csv
import io

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Risk Dashboard API"}

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

@router.get("/portfolio/{portfolio_id}/csv")
def get_csv(portfolio_id: int):
    # dummy logic — later query from DB
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Metric", "Value"])
    writer.writerow(["VaR 95%", 1200.00])
    writer.writerow(["VaR 99%", 1600.00])
    writer.writerow(["Stress Loss", 2000.00])
    return Response(content=output.getvalue(), media_type="text/csv")

@router.get("/risk/{portfolio_id}")
def run_risk(portfolio_id: int):
    result = calculate_var.delay({"id": portfolio_id})
    return {"task_id": result.id}

@router.get("/risk_result/{task_id}")
def run_risk(task_id: str):
    result = calculate_var.AsyncResult(task_id)
    return {"status": result.status, "result": result.result}