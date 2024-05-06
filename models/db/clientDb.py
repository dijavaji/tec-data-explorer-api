from pymongo import MongoClient
import utils.dataExplorer_constant

client = MongoClient(utils.dataExplorer_constant.DATABASE_URL)
#db = client[utils.dataExplorer_constant.DATABASE_DB]

#@staticmethod
def get_db() -> MongoClient:
    try:
        db = client[utils.dataExplorer_constant.DATABASE_DB]
        return db
    except:
        print("Error de conexion db")
    #finally:
        #db.close()