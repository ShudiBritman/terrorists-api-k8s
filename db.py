from pymongo import MongoClient
import os

import os

mongo_url = (
    f"mongodb://{os.environ['MONGO_USERNAME']}:"
    f"{os.environ['MONGO_PASSWORD']}@"
    f"{os.environ['MONGO_HOST']}:"
    f"{os.environ['MONGO_PORT']}/"
    f"{os.environ['MONGO_DB']}"
    f"?authSource={os.environ['MONGO_AUTH_SOURCE']}"
)


class Singelton:
    _instance = None
    @staticmethod
    def get_connection_to_mongo():
        if not Singelton._instance:
            client = MongoClient(mongo_url)
            Singelton._instance = 1
            return client


class Connector:
    @staticmethod    
    def get_database(client):
        db = client[os.environ['MONGO_DB']]
        return db
    

    @staticmethod
    def get_collection(database):
        collection = database['top_threats']
        return collection


    
client = Singelton.get_connection_to_mongo()

def get_coll_terrorist():
    top_threats_db = Connector.get_database(client)
    top_threats = Connector.get_collection(top_threats_db)
    return top_threats



def add_all_terrorist(terrorists: list[dict]):
    col = get_coll_terrorist()
    col.insert_many(terrorists)


