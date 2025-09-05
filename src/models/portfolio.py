# src/models/portfolio.py
from pydantic import BaseModel # pyright: ignore[reportMissingImports]
from typing import List
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime # pyright: ignore[reportMissingImports]
from sqlalchemy.orm import relationship # pyright: ignore[reportMissingImports]
from db.database import Base # pyright: ignore[reportMissingImports]
from datetime import datetime

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

class Portfolio(Base):
    __tablename__ = "portfolios"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    tickers = relationship("PortfolioTicker", back_populates="portfolio")

class PortfolioTicker(Base):
    __tablename__ = "portfolio_tickers"
    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"))
    ticker = Column(String)
    weight = Column(Float)
    portfolio = relationship("Portfolio", back_populates="tickers")