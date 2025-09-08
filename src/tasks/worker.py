# src/tasks/worker.py
from celery import Celery # pyright: ignore[reportMissingImports]

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery_app.task
def calculate_var(portfolio):
    print(f"Running risk job for {portfolio}")
    return {"VaR": 12345, "portfolio": portfolio}