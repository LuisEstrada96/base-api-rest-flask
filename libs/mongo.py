from pymongo import MongoClient
from config.config import db as config
class DB:
    def __init__(self):
        self.client = MongoClient(config['host'])
        self.client = self.client[config['name']]