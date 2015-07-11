import unittest
import destination_quiz_database_manager


class TestDestinationQuizDatabaseManager(unittest.TestCase):

    def setUp(self):
        destination_quiz_database_manager.create_tables()
        destination_quiz_database_manager.add_answer("answer_one")
        destination_quiz_database_manager.add_answer("answer_two")
        destination_quiz_database_manager.add_answer("answer_three")
        destination_quiz_database_manager.add_answer("answer_four")
        destination_quiz_database_manager.add_question(
            "This is Test question", 3)
        destination_quiz_database_manager.add_question(
            "This is Second Test question", 1)
        destination_quiz_database_manager.add_user("test_user")
        destination_quiz_database_manager.add_user("second_test_user")

    def test_add_answer(self):
        query = "SELECT Count(*) FROM answers WHERE answer_text = ?"
        destination_quiz_database_manager.cursor.execute(
            query, ("answer_two",))
        count = destination_quiz_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_question(self):
        query = "SELECT Count(*) FROM questions WHERE question_text = ?"
        destination_quiz_database_manager.cursor.execute(
            query, ("This is Test question",))
        count = destination_quiz_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_add_user(self):
        query = "SELECT Count(*) FROM users WHERE name = ?"
        destination_quiz_database_manager.cursor.execute(query, ("test_user",))
        count = destination_quiz_database_manager.cursor.fetchone()

        self.assertEqual(count[0], 1)

    def test_get_question_text(self):
        full_question = destination_quiz_database_manager.get_question(
            "test_user")

        self.assertEqual(full_question[0], "This is Test question")

    def test_get_question_right_answer_index(self):
        full_question = destination_quiz_database_manager.get_question(
            "test_user")
        answer_position = full_question[4]
        self.assertEqual(full_question[answer_position], 'answer_three')

    def test_get_question_right_answer(self):
        full_question = destination_quiz_database_manager.get_question(
            "test_user")

        self.assertEqual(full_question[full_question[4]], "answer_three")

    def test_get_questions_count(self):
        count = destination_quiz_database_manager.get_questions_count()

        self.assertEqual(count, 2)

    def test_get_answer_by_id(self):
        answer = destination_quiz_database_manager.get_answer_by_id(1)

        self.assertEqual(answer, "answer_one")

    def test_get_wrong_answers(self):
        answers = destination_quiz_database_manager.get_wrong_answers(1)

        self.assertEqual(len(answers), 3)

    def test_get_number_of_wrong_answers(self):
        destination_quiz_database_manager.next_question("test_user", False)
        number = destination_quiz_database_manager.get_number_of_wrong_answers(
            "test_user")
        self.assertEqual(number, 1)

    def test_get_last_answered(self):
        last_answered = destination_quiz_database_manager.get_last_answered(
            "test_user")
        self.assertEqual(last_answered, 1)

    def test_is_not_registered_false(self):
        existing_user = destination_quiz_database_manager.is_not_registered("test_user")
        self.assertFalse(existing_user)

    def test_is_not_registered_true(self):
        existing_user = destination_quiz_database_manager.is_not_registered("test_user1")
        self.assertTrue(existing_user)

    def test_next_question_true(self):
        destination_quiz_database_manager.next_question(
            "second_test_user", True)
        num_of_wrongs = destination_quiz_database_manager.get_number_of_wrong_answers("second_test_user")
        self.assertEqual(num_of_wrongs, 0)

    def tearDown(self):
        destination_quiz_database_manager.cursor.execute('DROP TABLE answers')
        destination_quiz_database_manager.cursor.execute(
            'DROP TABLE questions')
        destination_quiz_database_manager.cursor.execute('DROP TABLE users')

if __name__ == '__main__':
    unittest.main()
