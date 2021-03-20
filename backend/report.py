from random import randint, seed, sample
from migrations import create_hotels
import repository as db

seed(1)


def _calculate_daily_reservations(hotel):
    reservations = randint(1, hotel['rooms'])
    print(f"Hotel {hotel['name']} had {reservations} reservations. "
          f"Hotel is at {reservations / hotel['rooms'] * 100}% of its full capacity")


if __name__ == "__main__":
    # Fill DB with migration script
    create_hotels()

    hotels = db.find_hotels()

    # Print reservation details for every hotel
    [_calculate_daily_reservations(hotel) for hotel in sample(hotels, randint(1, len(hotels)))]
