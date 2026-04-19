import pymongo
import sys
import json
import pandas as pd
import os
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

# Load environment variables
load_dotenv()

# Get MongoDB URL from .env
MONGO_DB_URL = os.getenv("MONGO_DB_URL")


class NetworkDataExtract:

    def __init__(self):
        try:
            if MONGO_DB_URL is None:
                raise Exception("MONGO_DB_URL is not set in environment variables")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(inplace=True, drop=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongodb(self, records, database, collection):
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            db = mongo_client[database]
            col = db[collection]

            col.insert_many(records)

            return f"Data Inserted Successfully. Number of records inserted: {len(records)}"

        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    try:
        FILE_PATH = r"Network_Data\phisingData.csv"  # fixed path
        DATABASE_NAME = "NetworkSecurity"
        COLLECTION_NAME = "network_data"

        networkobject = NetworkDataExtract()

        records = networkobject.csv_to_json_converter(file_path=FILE_PATH)
        print(f"Records to insert: {len(records)}")

        result = networkobject.insert_data_to_mongodb(
            records=records,
            database=DATABASE_NAME,
            collection=COLLECTION_NAME
        )

        print(result)

    except Exception as e:
        logger.error(e)