from random import random
from tinydb import TinyDB, where

db = TinyDB('db.json')


def find_hotels():
    return db.all()


def find_hotel(hotel_id):
    return db.get(where('id') == int(hotel_id))


def create_hotel(hotel):
    hotel['id'] = int(random() * 100000)
    return db.insert(hotel)


def update_hotel(hotel_id, new_hotel):
    return db.update(new_hotel, where('id') == int(hotel_id))


def delete_hotel(hotel_id):
    return db.remove(where('id') == int(hotel_id))

