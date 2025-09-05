import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import Base, engine # pyright: ignore[reportMissingImports]
from pymongo import MongoClient # pyright: ignore[reportMissingImports]
from models import portfolio

Base.metadata.create_all(bind=engine)

# mongo's init
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URL)

market_db = client["market"]
market_data = market_db["prices"]  # Example collection

market_data.insert_one({"ticker": "AAPL", "price": 190.12, "ts": "2025-08-16"})