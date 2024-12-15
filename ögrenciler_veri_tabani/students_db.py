from mongodb_connect import MongoDBConnection

class StudentsDB(MongoDBConnection):
    def __init__(self, db_name):
        super().__init__()
        self.collection = self.database_getir(db_name)['ögrenciSkorlari']

    def ögrenci_skorlari_ekleme(self, data:dict):
        self.collection.insert_many(data)

    def toplam_puan_sorgulama(self):
        return self.collection.aggregate([
            {
                '$group':{
                    '_id':'$user',
                    "Toplam Puanlar":{'$sum':'$score'}
                }
            }
        ])
    
    # Ögrencilere göre gruplama yapin ve her ögrencinin kac tane ders aldigni toplayin
    def toplam_ders_sayisi(self):
        return self.collection.aggregate([
            {
                '$group':{
                    '_id':'$subject',
                    "Toplam Ders Sayisi":{'$sum': 1}
                }
            }
        ])
    
    # Ögrencileri _id olarak tanimlayin ve ögrencilere göre gruplayin. Buna karsilik olarak her ögrencinin toplam derslerden aldigi ortalama puani bulunuz.
    def ogrenci_ortalama_puan_hesaplama(self):
        return self.collection.aggregate([
            {
                "$group":{
                    '_id':'$user',
                    'Ortalama_Puanlar':{'$avg':'$score'}
                }
            }
        ])