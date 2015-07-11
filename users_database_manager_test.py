import unittest
import users_database_manager


class TestUsersDatabaseManager(unittest.TestCase):

    def setUp(self):
        users_database_manager.create_tables()
        users_database_manager.add_master_code(1111)
        users_database_manager.add_passenger(
            "pas_name", "password", "name@gmail.com")
        users_database_manager.add_administrator("admin_name", "password")
        users_database_manager.add_rich_client(
            "rich_name", "password", "rich plane")
        users_database_manager.add_user_destination(
            "pas_name", "Perfect Place")
        users_database_manager.add_user_ticket("pas_name", 1)

    def test_add_passenger(self):
        query = "SELECT Count(*) FROM passengers WHERE username = ?"
        users_database_manager.cursor.execute(query, ("pas_name",))
        count = users_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_administrator(self):
        query = "SELECT Count(*) FROM admins WHERE username = ?"
        users_database_manager.cursor.execute(query, ("admin_name",))
        count = users_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_rich_client(self):
        query = "SELECT Count(*) FROM rich_client WHERE username = ?"
        users_database_manager.cursor.execute(query, ("rich_name",))
        count = users_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_master_code(self):
        query = "SELECT Count(*) FROM master_codes"
        users_database_manager.cursor.execute(query)
        count = users_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_user_destination(self):
        query = "SELECT Count(*) FROM user_destinations WHERE username = ?"
        users_database_manager.cursor.execute(query, ("pas_name",))
        count = users_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_user_ticket(self):
        query = "SELECT Count(*) FROM users_tickets WHERE username = ?"
        users_database_manager.cursor.execute(query, ("pas_name",))
        count = users_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_get_travels(self):
        travel_count = users_database_manager.get_travels(
            "pas_name", "Perfect Place")

        self.assertEqual(1, travel_count)

    def test_increase_user_destination(self):
        travel_count_before = users_database_manager.get_travels(
            "pas_name", "Perfect Place")
        users_database_manager.increase_user_destination(
            "pas_name", "Perfect Place")
        travel_count_after = users_database_manager.get_travels(
            "pas_name", "Perfect Place")

        self.assertEqual(travel_count_before + 1, travel_count_after)

    def test_get_best_destination(self):
        users_database_manager.add_user_destination(
            "pas_name", "Not So Perfect Place")
        destination = users_database_manager.get_best_destination("pas_name")

        self.assertEqual("Perfect Place", destination)

    def test_get_admin(self):
        admin = users_database_manager.get_admin("admin_name")

        self.assertEqual("admin_name", admin[0])

    def test_get_passenger(self):
        passenger = users_database_manager.get_passenger("pas_name")

        self.assertEqual("pas_name", passenger[0])

    def test_get_rich_client(self):
        rich_client = users_database_manager.get_rich_client("rich_name")

        self.assertEqual("rich_name", rich_client[0])

    def test_check_code_true(self):
        there_is_check_code = users_database_manager.check_code(1111)

        self.assertEqual(True, there_is_check_code)

    def test_check_code_false(self):
        there_is_no_check_code = users_database_manager.check_code(2222)

        self.assertFalse(there_is_no_check_code)

    def test_check_ticket(self):
        there_is_ticket = users_database_manager.check_ticket(1, "pas_name")

        self.assertTrue(there_is_ticket)
    def test_get_email(self):
        email = users_database_manager.get_email("pas_name")

        self.assertEqual(email, "name@gmail.com")

    def tearDown(self):
        users_database_manager.cursor.execute('DROP TABLE passengers')
        users_database_manager.cursor.execute('DROP TABLE admins')
        users_database_manager.cursor.execute('DROP TABLE rich_client')
        users_database_manager.cursor.execute('DROP TABLE master_codes')
        users_database_manager.cursor.execute('DROP TABLE user_destinations')
        users_database_manager.cursor.execute('DROP TABLE users_tickets')

if __name__ == '__main__':
    unittest.main()
