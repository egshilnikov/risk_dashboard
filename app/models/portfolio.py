# app/models/portfolio.py
from pydantic import BaseModel # pyright: ignore[reportMissingImports]
from typing import List

class TickerWeight(BaseModel):
    ticker: str
    weight: float

class PortfolioInput(BaseModel):
    portfolio_name: str
    tickers: List[TickerWeight]

class PortfolioResult(BaseModel):
    portfolio_name: str
    var_95: float
    var_99: float
    stress_loss: float