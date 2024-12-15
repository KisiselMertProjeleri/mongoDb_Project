from mongodb_connect import MongoDBConnection

class Inventory(MongoDBConnection):
    def __init__(self,db_name):
        super().__init__()
        self.collection = self.database_getir(db_name)['inventory']

    def insert_inventory_data(self, data):
        self.collection.insert_many(data)

    def update_inventory_data(self, item, updates):
        self.collection.update_one(
            {'item':item},
            {   
                '$set':updates,
                '$currentDate':{'lastModified':True}
            }  
        )
    def update_inventory_bulk(self, query, updates):
        self.collection.update_many(
            query,
            {'$set':updates,'$currentDate':{'lastModified':True}}
        )