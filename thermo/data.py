from config import DATABASE_URI, SENSOR_URI, DB
import pandas as pd
import pymongo
import requests


def get_live_reading():
    reading = requests.get(SENSOR_URI)
    if reading.status_code == 200:
        return reading
    return None


def get_last_readings():
    with pymongo.MongoClient(DATABASE_URI) as client:
        db = client['thermo']
        result = db.reading.find_one({}, sort=[('_id', pymongo.DESCENDING)])
        # print(result)
    return result


def find_date_reading(start_date, end_date):
    # print(f"Getting readings from {start_date} to {end_date}")
    with pymongo.MongoClient(DATABASE_URI) as client:
        db = client[DB['name']]
        cursor = db[DB['collection']].find({'timestamp': {'$lt': end_date, '$gte': start_date}})
        df = pd.DataFrame(list(cursor))
    return df
