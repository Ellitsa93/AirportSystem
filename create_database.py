import users_database_manager
import lines_database_manager
import destination_quiz_database_manager


def main():
    users_database_manager.create_tables()
    lines_database_manager.create_tables()
    destination_quiz_database_manager.create_tables()

    add_users_data()
    add_lines_data()
    add_destination_quiz_data()


def add_users_data():
    users_database_manager.add_master_code(1111)
    users_database_manager.add_master_code(2222)

    users_database_manager.add_passenger(
        "Passenger First", "pas", "first@passenger.com")
    users_database_manager.add_passenger(
        "Passenger Second", "pas", "second@passenger.com")
    users_database_manager.add_passenger(
        "Passenger Third", "pas", "third@passenger.com")

    users_database_manager.add_administrator("Admin First", "pas")
    users_database_manager.add_administrator("Admin Second", "pas")
    users_database_manager.add_administrator("Admin Third", "pas")

    users_database_manager.add_rich_client("Rich First", "pas", "Plane First")
    users_database_manager.add_rich_client(
        "Rich Second", "pas", "Plane Second")
    users_database_manager.add_rich_client("Rich Third", "pas", "Plane Third")

    users_database_manager.add_user_destination("Passenger First", "Bora Bora")
    users_database_manager.add_user_destination("Passenger First", "Tahiti")
    users_database_manager.add_user_destination(
        "Passenger Second", "Bora Bora")

    users_database_manager.add_user_ticket("Passenger First", 2)
    users_database_manager.add_user_ticket("Passenger Third", 4)


def add_lines_data():
    lines_database_manager.add_runway(1, "19-Jul-2015 13:31")
    lines_database_manager.add_runway(0, "31-Dec-2050 23:59")
    lines_database_manager.add_runway(1, "30-Aug-2015 19:18")
    lines_database_manager.add_runway(1, "26-Apr-2016 22:30")

    lines_database_manager.add_flight("Bora Bora", "15-Jul-2015 13:31")
    lines_database_manager.add_flight("Tahiti", "12-Jul-2015 10:30")

    lines_database_manager.add_seat(1, 1, 103, 4, 7, 5)
    lines_database_manager.add_seat(1, 2, 201, 0, 8, 3)
    lines_database_manager.add_seat(1, 3, 100, 5, 6, 4)
    lines_database_manager.add_seat(1, 4, 109, 6, 9, 6)
    lines_database_manager.add_seat(1, 5, 189, 2, 5, 2)
    lines_database_manager.add_seat(1, 6, 167, 1, 3, 6)
    lines_database_manager.add_seat(1, 7, 148, 2, 4, 2)

    lines_database_manager.add_seat(2, 1, 25, 1, 4, 2)
    lines_database_manager.add_seat(2, 2, 45, 2, 3, 2)
    lines_database_manager.add_seat(2, 3, 32, 1, 3, 3)
    lines_database_manager.add_seat(2, 4, 15, 3, 5, 2)
    lines_database_manager.add_seat(2, 5, 65, 2, 3, 2)

    lines_database_manager.add_promo_code(1234, 10)
    lines_database_manager.add_promo_code(5678, 15)


def add_destination_quiz_data():
    destination_quiz_database_manager.add_answer("answer one")
    destination_quiz_database_manager.add_answer("answer two")
    destination_quiz_database_manager.add_answer("answer three")
    destination_quiz_database_manager.add_answer("answer four")
    destination_quiz_database_manager.add_answer("answer five")

    destination_quiz_database_manager.add_question("question one", 1)
    destination_quiz_database_manager.add_question("question two", 2)
    destination_quiz_database_manager.add_question("question three", 3)


if __name__ == '__main__':
    main()
