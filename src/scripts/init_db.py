from db.database import Base, engine # pyright: ignore[reportMissingImports]
from pymongo import MongoClient # pyright: ignore[reportMissingImports]
import os

Base.metadata.create_all(bind=engine)

# mongo's init
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017/")
client = MongoClient(MONGO_URL)

market_db = client["market"]
market_data = market_db["prices"]  # Example collection

market_data.insert_one({"ticker": "AAPL", "price": 190.12, "ts": "2025-08-16"})