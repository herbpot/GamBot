from pymongo import MongoClient

db = MongoClient(
    host="localhost",
    port=27017
).GamBot

class User:
    collection = db.user
    def __init__(self, userId, DBId) -> None:
        self._id = userId
        self.DBId = DBId
    
    def save(self):
        User.collection.insert_one(self.__dict__)

    def find(q:dict):
        return User.collection.find(q)
    
    def find_one(q:dict):
        return User.collection.find_one(q)
    
class Diary:
    collection = db.diary
    def __init__(self, user: dict, context: str, files: list) -> None:
        d = context.split()
        self.user = user['_id']
        self.title = d[0]
        self.context = d[1:]
        self.files = files
        
    def save(self):
        Diary.collection.insert_one(self.__dict__)

    def find(q:dict):
        return Diary.collection.find(q)
        
    def find_one(q:dict):
        return Diary.collection.find_one(q)