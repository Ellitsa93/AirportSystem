import unittest
import users


class UsersTests(unittest.TestCase):

    def test_create_seats_list_taken(self):
        seats = [[1, 0], [2, 1], [3, 0], [4, 0], [5, 1]]
        seats_list = users.create_seats_list(seats)

        self.assertEqual(seats_list[0][1], "X")

    def test_create_seats_list_free(self):
        seats = [[1, 0], [2, 1], [3, 0], [4, 0], [5, 1]]
        seats_list = users.create_seats_list(seats)

        self.assertEqual(seats_list[0][0], "1")

    def test_create_seats_list_second_row(self):
        seats = [[1, 0], [2, 1], [3, 0], [4, 0], [5, 1]]
        seats_list = users.create_seats_list(seats)

        self.assertEqual(seats_list[1][0], "X")

    def test_create_seats_list_second_row_missing(self):
        seats = [[1, 0], [2, 1], [3, 0], [4, 0], [5, 1]]
        seats_list = users.create_seats_list(seats)

        self.assertEqual(seats_list[1][3], "")

    def test_create_seats_list_corridor(self):
        seats = [[1, 0], [2, 1], [3, 0], [4, 0], [5, 1]]
        seats_list = users.create_seats_list(seats)

        self.assertEqual(seats_list[0][2], "")

    def test_create_seat_for_showing_taken(self):
        text = users.create_seat_for_showing([12, 1])

        self.assertEqual(text, "X")

    def test_create_seat_for_showing_taken(self):
        text = users.create_seat_for_showing([12, 0])

        self.assertEqual(text, "12")

    def test_calculate_time_before_true_minutes(self):
        result = users.calculate_time_before(
            "12-Oct-2015 12:30", "12-Oct-2015 12:31")
        self.assertTrue(result)

    def test_calculate_time_before_true_hours(self):
        result = users.calculate_time_before(
            "12-Oct-2015 12:30", "12-Oct-2015 13:30")
        self.assertTrue(result)

    def test_calculate_time_before_true_date(self):
        result = users.calculate_time_before(
            "12-Oct-2015 12:30", "13-Oct-2015 12:30")
        self.assertTrue(result)

    def test_calculate_time_before_true_month(self):
        result = users.calculate_time_before(
            "12-Oct-2015 12:30", "12-Dec-2015 12:30")
        self.assertTrue(result)

    def test_calculate_time_before_true_year(self):
        result = users.calculate_time_before(
            "12-Oct-2015 12:30", "12-Oct-2016 12:30")
        self.assertTrue(result)

    def test_calculate_time_before_false_minutes(self):
        result = users.calculate_time_before(
            "12-Oct-2015 12:31", "12-Oct-2015 12:30")
        self.assertFalse(result)

    def test_calculate_time_before_false_hours(self):
        result = users.calculate_time_before(
            "12-Oct-2015 13:30", "12-Oct-2015 12:30")
        self.assertFalse(result)

    def test_calculate_time_before_false_date(self):
        result = users.calculate_time_before(
            "13-Oct-2015 12:30", "12-Oct-2015 12:30")
        self.assertFalse(result)

    def test_calculate_time_before_false_month(self):
        result = users.calculate_time_before(
            "12-Dec-2015 12:30", "12-Oct-2015 12:30")
        self.assertFalse(result)

    def test_calculate_time_before_false_year(self):
        result = users.calculate_time_before(
            "12-Oct-2016 12:30", "12-Oct-2015 12:30")
        self.assertFalse(result)

    def test_calculate_time_after_true_minutes(self):
        result = users.calculate_time_after(
            "12-Oct-2015 12:31", "12-Oct-2015 12:30")
        self.assertTrue(result)

    def test_calculate_time_after_true_hours(self):
        result = users.calculate_time_after(
            "12-Oct-2015 13:30", "12-Oct-2015 12:30")
        self.assertTrue(result)

    def test_calculate_time_after_true_date(self):
        result = users.calculate_time_after(
            "13-Oct-2015 12:30", "12-Oct-2015 12:30")
        self.assertTrue(result)

    def test_calculate_time_after_true_month(self):
        result = users.calculate_time_after(
            "12-Dec-2015 12:30", "12-Oct-2015 12:30")
        self.assertTrue(result)

    def test_calculate_time_after_true_year(self):
        result = users.calculate_time_after(
            "12-Oct-2016 12:30", "12-Oct-2015 12:30")
        self.assertTrue(result)

    def test_calculate_time_after_false_minutes(self):
        result = users.calculate_time_after(
            "12-Oct-2015 12:30", "12-Oct-2015 12:31")
        self.assertFalse(result)

    def test_calculate_time_after_false_hours(self):
        result = users.calculate_time_after(
            "12-Oct-2015 12:30", "12-Oct-2015 13:30")
        self.assertFalse(result)

    def test_calculate_time_after_false_date(self):
        result = users.calculate_time_after(
            "12-Oct-2015 12:30", "13-Oct-2015 12:30", )
        self.assertFalse(result)

    def test_calculate_time_after_false_month(self):
        result = users.calculate_time_after(
            "12-Oct-2015 12:30", "12-Dec-2015 12:30")
        self.assertFalse(result)

    def test_calculate_time_after_false_year(self):
        result = users.calculate_time_after(
            "12-Oct-2015 12:30", "12-Oct-2016 12:30")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
