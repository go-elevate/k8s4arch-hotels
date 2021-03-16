from tinydb import TinyDB, where
import os

db = TinyDB(os.getenv('DB_PATH', default='db.json'))


def db_full():
    return len(db) > 0


def find_hotels():
    return db.all()


def find_hotel(hotel_id):
    return db.get(where('id') == int(hotel_id))


def create_hotel(hotel):
    return db.insert(hotel)


def update_hotel(hotel_id, new_hotel):
    return db.update(new_hotel, where('id') == int(hotel_id))


def delete_hotel(hotel_id):
    return db.remove(where('id') == int(hotel_id))
