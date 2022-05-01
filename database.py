import pymongo
import log
lg = log.logFile()
class mongoDatabase:
    try:
        client = pymongo.MongoClient("mongodb+srv://ineuron:ineuron@cluster0.n2xzc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    except Exception as e:
        lg.logging.exception(e)

    def __init__(self,dbname,collections,documents=None):
        self.dbname = dbname
        self.collections = collections
        self.documents = documents
        self.coll = ''

    def checkDB(self):
        if self.dbname in self.client.list_database_names():
            lg.logging.info("{} Database already Exist".format(self.dbname))
            #print("{} Database already Exist".format(self.dbname))
        else:
            lg.logging.info("Creating Database :" + self.dbname)
            #print("Creating Database :" + self.dbname)
            self.dbname = self.client['ineuron']

    def createCollection(self):
        if self.collections in self.client[self.dbname].list_collection_names():
            lg.logging.info("{} Collection already Exist".format(self.collections))
            #print("{} Collection already Exist".format(self.collections))
        else:
            lg.logging.info("Creating Collection : "+self.collections)
            #print("Creating Collection : "+self.collections)
            db = self.client[self.dbname]
            self.coll = db[self.collections]

    def insertDocuments(self):
        db = self.client[self.dbname]
        self.coll = db[self.collections]
        lg.logging.info("Inserting data into mongodb")
        #print("Inserting data into mongodb")
        self.coll.insert_many(self.documents)

    def getCollection(self):
        db = self.client[self.dbname]
        col = db[self.collections]
        return col.find({},{'_id':False})

    def deleteDB(self):
        pass

    def deleteCollection(self):
        pass

