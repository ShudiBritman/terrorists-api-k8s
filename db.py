from pymongo import MongoClient
import os

DB_CONFIG = {
    "host": os.getenv("MONGO_HOST", "localhost")
    }

class Singelton:
    _instance = None
    @staticmethod
    def get_connection_to_mongo():
        if not Singelton._instance:
            client = MongoClient(f"mongodb://{DB_CONFIG}, 27017")
            Singelton._instance = 1
            return client


class Connector:
    @staticmethod    
    def get_database(client):
        database = client['threat_db']
        return database
    

    @staticmethod
    def get_collection(database):
        collection = database['top_threats']
        return collection


    
client = Singelton.get_connection_to_mongo()

def get_coll_terrorist():
    top_threats_db = Connector.get_database(client)
    top_threats = Connector.get_collection(top_threats_db)
    return top_threats


def add_terrorist(terrorist_data):
    col_terrorist = get_coll_terrorist()
    insert_terrorist = col_terrorist.insert_one(terrorist_data)
    return insert_terrorist


def add_all_terrorist(data):
    for terrorist in data:
        result = add_terrorist(terrorist)
    return result

