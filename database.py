# from pymongo import MongoClient
from app import db

class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String())
    room = db.Column(db.String())

    def __init__(self, username, room):
        self.username = username
        self.room = room


# client = MongoClient(host="mongodb+srv://test:authenticate@chatapp.7biyn.mongodb.net/<dbname>?retryWrites=true&w=majority")

# chat_db = client.get_database("chatapp")

# users_col = chat_db.get_collection("users")

# def add_user(username, room):
#     users_col.insert_one({'_id' : username, 'room' : room})
