# app/db/mongo.py
from pymongo import MongoClient # pyright: ignore[reportMissingImports]
import os

client = MongoClient(os.getenv("MONGO_URL"))
mongo_db = client["risk_data"]