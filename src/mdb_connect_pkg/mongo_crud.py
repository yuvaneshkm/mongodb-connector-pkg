# importing necessary libraries:
from pathlib import Path
import pandas as pd
from pymongo.mongo_client import MongoClient
import json
import warnings
warnings.filterwarnings('ignore')


# creatring a class for mongodb connection:
class MongoDBConnection:

    # constructor:
    def __init__(self, client_url: str, database_name: str, collection_name: str):
        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name

    # mongo client:
    def create_mongo_client(self):
        self.client = MongoClient(self.client_url)

    # database:
    def database_(self):
        self.db = self.client[self.database_name]

    # collection:
    def collection_(self):
        coll = self.db[self.collection_name]
        return coll

    # insert single record:
    def single_insert(self, record: dict):
        coll = self.collection_()
        coll.insert_one(record)

    # insert bulk record:
    def bulk_insert(self, file_path: str):
        file_path = str(Path(file_path))

        if file_path.split('.')[-1]=='json':
            with open(file_path, 'r') as file:
                json_file_data = json.load(file)
            file.close()
            coll = self.collection_()
            coll.insert_many(json_file_data)

        elif file_path.split('.')[-1] == 'csv':
            df = pd.read_csv(file_path)
            csv_file_data = df.to_dict(orient='records')
            coll = self.collection_()
            coll.insert_many(csv_file_data)

    # load the collection as a dataframe:
    def load_data(self):
        collection = self.collection_()
        data = collection.find()
        df = pd.DataFrame(list(data))
        df.drop('_id', axis=1, inplace=True)
        return df

    # updating the data:
    def update_data(self, *query):
        collection = self.collection_()
        collection.update_many(*query)

    # delete the data:
    def delete_record(self, *query):
        collection = self.collection_()
        collection.delete_many(*query)

    # drop the entire collection:
    def drop_collection(self):
        collection = self.collection_()
        collection.drop()

    # drop the entire database:
    def drop_database(self):
        self.client.drop_database(self.database_name)
