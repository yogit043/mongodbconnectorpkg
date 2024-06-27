import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

dataBase = client['neurolabDB']

collection = dataBase['Products']

d = {"companyName":"yogit" , "product":"affordable ai","courseOffered":"Machine Learning"}
rec = collection.insert_one(d)
all_record = collection.find()

for idx,record in enumerate(all_record):
    print(f"Record {idx}: {record}")