from pymongo import MongoClient

db_client = MongoClient("localhost", 27017)

db = db_client.desarrollo_db

