from random import randint, seed, sample
import logging
import subprocess
import repository as db

log = logging.getLogger('report')
seed(1)


def _calculate_daily_reservations(hotel):
    reservations = randint(0, hotel['rooms'])
    log.info(f"Hotel {hotel['name']} had {reservations} reservations. "
             f"Hotel is at {reservations/hotel['rooms']*100}% of its full capacity")


if __name__ == "__main__":

    # Fill DB with migration script
    subprocess.call('migrations.py', shell=True)

    hotels = db.find_hotels()

    # Print reservation details for every hotel
    [_calculate_daily_reservations(hotel) for hotel in sample(hotels, randint(1, len(hotels)))]
