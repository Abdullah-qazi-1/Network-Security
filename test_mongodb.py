from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# .env file load karo - ZAROORI HAI
load_dotenv()

# .env se URL lo
uri = os.getenv("MONGO_DB_URL")

# Connect karo
client = MongoClient(uri, server_api=ServerApi('1'))

# Ping test
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)