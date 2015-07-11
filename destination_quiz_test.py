import unittest
import destination_quiz


class TestDestinationQuiz(unittest.TestCase):

    def test_check_answer_a(self):
        result = destination_quiz.check_answer("A", 1)

        self.assertTrue(result)

    def test_check_answer_b(self):
        result = destination_quiz.check_answer("B", 2)

        self.assertTrue(result)

    def test_check_answer_c(self):
        result = destination_quiz.check_answer("C", 3)

        self.assertTrue(result)

    def test_check_answer_false_a_2(self):
        result = destination_quiz.check_answer("A", 2)

        self.assertFalse(result)

    def test_check_answer_false_a_3(self):
        result = destination_quiz.check_answer("A", 3)

        self.assertFalse(result)

    def test_check_answer_false_b_1(self):
        result = destination_quiz.check_answer("B", 1)

        self.assertFalse(result)

    def test_check_answer_false_b_3(self):
        result = destination_quiz.check_answer("B", 3)

        self.assertFalse(result)

    def test_check_answer_false_c_1(self):
        result = destination_quiz.check_answer("C", 1)

        self.assertFalse(result)

    def test_check_answer_false_c_2(self):
        result = destination_quiz.check_answer("C", 2)

        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
