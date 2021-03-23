import json
import pymongo

client = pymongo.MongoClient("mongodb://mongoadmin:secret@172.17.0.2")

db = client['db_name']

with open('./segments.json', 'r') as f:
    segments = json.load(f)
    segments = list(filter(lambda x: x['fwdMaxSpeed'] != 50, segments))
    operations = [pymongo.operations.ReplaceOne(
        filter={"id": doc["id"]}, 
        replacement=doc,
        upsert=True
        ) for doc in segments]

    result = db.segments.bulk_write(operations)

client.close()
