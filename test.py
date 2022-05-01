import database
import pandas as pd
import pymongo
db = database.mongoDatabase(dbname='ineuron',collections='teachers')
#client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron@cluster0.n2xzc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

#db = client['ineuron']

#coll = db['teachers']
#x = coll.find()
x = db.getCollection()
name = []
for i in x:
    name.append(i)
df = pd.DataFrame(name)
print(df[['Name','Email','Bio']])