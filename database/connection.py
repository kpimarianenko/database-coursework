import pymongo
import os
from repositories.base_repository import BaseRepository
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DB_URL')
db_name = os.getenv('DB_NAME')

client = pymongo.MongoClient(db_url)
db = client[db_name]
