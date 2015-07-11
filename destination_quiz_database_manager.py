import sqlite3
import random

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()


def create_tables():
    create_answers_table()
    create_questions_table()
    create_users_table()


def create_questions_table():
    query = """CREATE TABLE IF NOT EXISTS
        questions(id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT,
            right_answer_id INTEGER,
            FOREIGN KEY(right_answer_id) REFERENCES andwers(id))"""

    cursor.execute(query)


def create_answers_table():
    query = """CREATE TABLE IF NOT EXISTS
        answers(id INTEGER PRIMARY KEY AUTOINCREMENT,
            answer_text TEXT)"""

    cursor.execute(query)


def create_users_table():
    query = """CREATE TABLE IF NOT EXISTS
        users(id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            last_answered_question INTEGER,
            number_of_wrong_answers INTEGER)"""

    cursor.execute(query)


def add_answer(text_of_the_answer):
    query = "INSERT INTO answers (answer_text) values (?)"

    cursor.execute(query, (text_of_the_answer,))
    conn.commit()


def add_question(text_of_the_question, right_answer):
    query = """INSERT INTO questions(question_text, right_answer_id)
    values (?, ?)"""

    cursor.execute(query, (text_of_the_question, right_answer))
    conn.commit()


def add_user(name):
    query = """INSERT into users
    (name, last_answered_question, number_of_wrong_answers)
    values (?, ?, ?)"""

    cursor.execute(query, (name, 1, 0))
    conn.commit()


def get_answer_by_id(id):
    query = "SELECT answer_text FROM answers WHERE id = ?"
    cursor.execute(query, (id,))
    answer = cursor.fetchone()
    return answer[0]


def get_wrong_answers(right_id):
    query = "SELECT id, answer_text FROM answers WHERE id <> ?"
    cursor.execute(query, (right_id,))
    answer = cursor.fetchall()
    return answer


def get_questions_count():
    query = "SELECT Count(*) FROM questions"
    cursor.execute(query)
    count = cursor.fetchone()
    return count[0]


def get_last_answered(username):
    query = "SELECT last_answered_question FROM users WHERE name == ?"
    cursor.execute(query, (username,))
    last_answered = cursor.fetchone()
    return last_answered[0]


def get_number_of_wrong_answers(username):
    query = "SELECT number_of_wrong_answers FROM users WHERE name = ?"
    cursor.execute(query, (username, ))
    count = cursor.fetchone()
    if count is None:
        return 0
    return count[0]


def get_question(username):
    query = """SELECT question_text, right_answer_id
    FROM questions AS q, users AS u
    WHERE q.id = (SELECT last_answered_question
        FROM users WHERE name = ?)"""
    cursor.execute(query, (username,))

    question = cursor.fetchone()
    right_answer = get_answer_by_id(question[1])
    wrong_answers = get_wrong_answers_list(question[1])

    return get_question_with_answers(question, wrong_answers, right_answer)


def get_wrong_answers_list(id):
    all_wrong_answers = get_wrong_answers(id)

    first_index = id
    while(first_index == id):
        first_index = random.randint(1, len(all_wrong_answers) + 1)
    second_index = id
    while(second_index == id or second_index == first_index):
        second_index = random.randint(1, len(all_wrong_answers) + 1)

    return list(filter(lambda x: x[0] == first_index or x[0] == second_index,
                       all_wrong_answers))


def get_question_with_answers(question, wrong_answers, right_answer):
    right_position = random.randint(1, 3)
    if right_position == 1:
        question_and_answers = [question[0], right_answer,
                                wrong_answers[0][1], wrong_answers[1][1]]
    elif right_position == 2:
        question_and_answers = [question[0], wrong_answers[0][1], right_answer,
                                wrong_answers[1][1]]
    else:
        question_and_answers = [question[0], wrong_answers[0][1],
                                wrong_answers[1][1], right_answer]
    question_and_answers.append(right_position)
    return question_and_answers


def next_question(username, is_correct):
    last_answered = get_last_answered(username)
    if is_correct is True:
        query = """UPDATE users SET last_answered_question = ?
        WHERE name == ?"""
        cursor.execute(query, (last_answered + 1, username,))
    else:
        wrongs = get_number_of_wrong_answers(username)
        query = """UPDATE users SET last_answered_question = ?,
        number_of_wrong_answers = ? WHERE name == ?"""
        cursor.execute(query, (last_answered + 1, wrongs + 1, username))
    conn.commit()


def is_not_registered(username):
    query = "SELECT id FROM users WHERE name = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()
    if user is None:
        return True
    return False
