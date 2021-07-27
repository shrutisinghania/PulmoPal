import base64
import random
def encode(name):
    sample_string_bytes = name.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string
from pymongo import MongoClient


client = MongoClient("mongodb+srv://ShipIt:root@cluster0.cey16.mongodb.net/ShipIt?retryWrites=true&w=majority")
db = client.get_database('ShipIt')
records = db.Analysis
for x in records.find({},{ "age": 1,"location":1,"first_name":1,"last_name":1 }):
  print(x)
'''myquery = { "location": "Union territory" }

x = records.delete_many(myquery)

print(x.deleted_count, " documents deleted.")'''
'''for i in range(1000):
    first_name = 'Satya'+str(i)
    last_name = 'Guch'+str(i)
    age = random.randint(15,90)
    gender = random.choice(['Male', 'Female'])
    location = random.choice(['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal','Union territory','Andaman and Nicobar Islands','Chandigarh','Delhi','Jammu and Kashmir','Ladakh','Lakshadweep','Puducherry'])
    predictionResult = random.choice(['Covid', 'Pneumonia'])
    dictionary = {'first_name': encode(first_name), 'last_name': encode(last_name), 'age': age, 'gender': gender, 'location' : location, 'predictionResult': predictionResult}
    records.insert_one(dictionary)
print(records.count_documents({}))


mycol = db["Analysis"]

#for x in mycol.find():
agg_result= mycol.aggregate([ {"$match":{"predictionResult": "Covid" }}, {"$group":{"_id":"$location", "Covid":{"$sum":1}}}] ) 
            

agg_result= mycol.aggregate([  {"$match":{"predictionResult": "Covid" }}, {"$group":{"_id":"$location", "Number":{"$sum":1}}} ,{ "$sort" : {"_id" : 1  }}] ) 
stats = [] 
j = 0

for i in agg_result: 
    print(i)
    l = []
    l = list(i.values())
    l.append(j+1)
    stats.append(l)

print (stats)'''