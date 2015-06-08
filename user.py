import users_database_manager


class User:

    def __init__(self, username, password):
        pass

    def show_flight_list(self, start_date, end_date, destination):
        pass

    def show_seats_scheme(self, flight_id):
        pass

    def get_ticket(self, flight_id, seat_number, extras):
        add_extras_for_ticket(extras)
        pass

    def add_extras_for_ticket(self, extras):
        pass

    def show_runway_scheme(self, start_date, end_date):
        pass

    def add_promo_key(self, promo_key):
        pass

    def get_promo_flights(self, destination):
        pass
