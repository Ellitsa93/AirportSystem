import unittest
import lines_database_manager


class TestLinesDatabaseManager(unittest.TestCase):

    def setUp(self):
        lines_database_manager.create_tables()
        lines_database_manager.add_flight("Perfect Place", "21-Jul-2015 12:56")
        lines_database_manager.add_runway(0, "31-Dec-2050 23:59")
        lines_database_manager.add_runway(1, "12-Nov-2015 13:45")
        lines_database_manager.add_seat(1, 1, 10, 1, 1, 1)
        lines_database_manager.add_seat(1, 2, 15, 1, 2, 1)
        lines_database_manager.add_seat(1, 3, 7, 1, 1, 1)
        lines_database_manager.add_seat(1, 4, 11, 2, 2, 2)
        lines_database_manager.add_promo_code(1111, 10)

    def test_add_extras(self):
        query = "SELECT Count(*) FROM extras"
        lines_database_manager.cursor.execute(query, ())
        count = lines_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 4)

    def test_add_flight(self):
        query = "SELECT Count(*) FROM flights WHERE id = ?"
        lines_database_manager.cursor.execute(query, (1,))
        count = lines_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_runway(self):
        query = "SELECT Count(*) FROM runway WHERE id = ?"
        lines_database_manager.cursor.execute(query, (1,))
        count = lines_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_seat(self):
        query = "SELECT Count(*) FROM seats WHERE flight_id = ? and num = ?"
        lines_database_manager.cursor.execute(query, (1, 2))
        count = lines_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_promo_code(self):
        query = "SELECT Count(*) FROM promo_codes WHERE code = ?"
        lines_database_manager.cursor.execute(query, (1111, ))
        count = lines_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_is_promo_code_correct_true(self):
        pomo_code_correct = lines_database_manager.is_promo_code_correct(1111)

        self.assertTrue(pomo_code_correct)

    def test_is_promo_code_correct_false(self):
        pomo_code_not_correct = lines_database_manager.is_promo_code_correct(
            1234)

        self.assertFalse(pomo_code_not_correct)

    def test_get_promo_code_percent(self):
        persent = lines_database_manager.get_promo_code_percent(1111)

        self.assertEqual(persent, 10)

    def test_get_seat_price(self):
        price = lines_database_manager.get_seat_price(1, 2)

        self.assertEqual(price, 15)

    def test_get_free_runways(self):
        runways = lines_database_manager.get_free_runways()

        self.assertEqual(runways[0][0], 2)

    def test_get_flights(self):
        flights = lines_database_manager.get_flights("Perfect Place")

        self.assertEqual(flights[0][0], 1)

    def test_get_seats_count(self):
        seats = lines_database_manager.get_seats(1)

        self.assertEqual(len(seats), 4)

    def test_get_seats(self):
        seats = lines_database_manager.get_seats(1)
        self.assertEqual(seats[2][0], 3)

    def test_get_extras_prices_headphones(self):
        prices = lines_database_manager.get_extras_prices(1, 2)

        self.assertEqual(prices[0], 1)

    def test_get_extras_prices_champagne(self):
        prices = lines_database_manager.get_extras_prices(1, 2)

        self.assertEqual(prices[1], 2)

    def test_get_extras_prices_food(self):
        prices = lines_database_manager.get_extras_prices(1, 2)

        self.assertEqual(prices[2], 1)

    def test_get_ticket_id(self):
        id = lines_database_manager.get_ticket_id(1, 2)
        self.assertEqual(id, 2)

    def test_set_seat_sold(self):
        sold = lines_database_manager.set_seat_sold(1, 2)
        query = "SELECT sold FROM seats WHERE flight_id = ? and num = ?"
        lines_database_manager.cursor.execute(query, (1, 2))
        seat = lines_database_manager.cursor.fetchone()

        self.assertEqual(seat[0], 1)

    def test_set_extras_to_seat_headphones(self):
        lines_database_manager.set_extras_to_seat(1, 3, 1, 0, 0)
        query = "SELECT headphones FROM seats WHERE flight_id = ? and num = ?"
        lines_database_manager.cursor.execute(query, (1, 3))
        headphones = lines_database_manager.cursor.fetchone()

        self.assertEqual(headphones[0], 1)

    def test_set_extras_to_seat_champagne(self):
        lines_database_manager.set_extras_to_seat(1, 3, 1, 1, 0)
        query = "SELECT champagne FROM seats WHERE flight_id = ? and num = ?"
        lines_database_manager.cursor.execute(query, (1, 3))
        champagne = lines_database_manager.cursor.fetchone()

        self.assertEqual(champagne[0], 1)

    def test_set_extras_to_seat_headphones(self):
        lines_database_manager.set_extras_to_seat(1, 3, 1, 1, 1)
        query = "SELECT food FROM seats WHERE flight_id = ? and num = ?"
        lines_database_manager.cursor.execute(query, (1, 3))
        food = lines_database_manager.cursor.fetchone()

        self.assertEqual(food[0], 1)

    def test_get_destination(self):
        destination = lines_database_manager.get_destination(1)

        self.assertEqual(destination, "Perfect Place")

    def test_get_runway(self):
        runway = lines_database_manager.get_runway(1)

        self.assertEqual(runway[0], 0)

    def test_is_ticket_taken_true(self):
        lines_database_manager.set_seat_sold(1,2)
        is_taken = lines_database_manager.is_ticket_taken(1, 2)

        self.assertTrue(is_taken)

    def test_is_ticket_taken_false(self):
        is_taken = lines_database_manager.is_ticket_taken(1, 1)

        self.assertFalse(is_taken)

    def test_set_permission_given_at_time(self):
        lines_database_manager.set_permission_given_at_time(2, "12-Oct-2015 12:30")
        runway = lines_database_manager.get_runway(2)

        self.assertEqual(runway[1], "12-Oct-2015 12:30")

    def test_make_runway_free(self):
        lines_database_manager.make_runway_free(1)
        runway = lines_database_manager.get_runway(1)

        self.assertEqual(runway[0], 1)

    def tearDown(self):
        lines_database_manager.cursor.execute('DROP TABLE seats')
        lines_database_manager.cursor.execute('DROP TABLE flights')
        lines_database_manager.cursor.execute('DROP TABLE extras')
        lines_database_manager.cursor.execute('DROP TABLE promo_codes')
        lines_database_manager.cursor.execute('DROP TABLE runway')


if __name__ == '__main__':
    unittest.main()
