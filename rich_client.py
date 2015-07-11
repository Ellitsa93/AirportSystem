import users
import rich_people_calendar
import users_database_manager
from datetime import datetime
import lines_database_manager
from prettytable import PrettyTable


def show_rich_client_options(username):
    while True:
        show_options()
        choice = input("Make your choice: ")
        choice = int(choice)
        if choice == 1:
            users.show_flight_list()
        elif choice == 2:
            users.show_seats_scheme()
        elif choice == 3:
            get_ticket(username)
        elif choice == 4:
            users.show_free_runways()
        elif choice == 5:
            check_for_free_runway()
        elif choice == 6:
            make_runway_free()
        elif choice == 7:
            break
        else:
            print("\nWrong number!")


def show_options():
    print("\nTo see flights press 1")
    print("To see seats for a flight press 2")
    print("To buy a ticket press 3")
    print("To see runways press 4")
    print("To check for free runway press 5")
    print("To make runway free press 6")
    print("To exit press 7")


def get_ticket(username):
    ticket = users.settng_ticket_sold_procedure(username)
    if len(ticket) == 0:
        print("This ticket is already taken. Pick anothe one. \
            For more information look at the seats table.")


def register_if_possible(name, password):
    plane_name = input("Enter name of the plane: ")
    plane_name = str(plane_name)
    if users.is_not_duplicated(name):
        register(name, password, plane_name)


def register(name, password, plane_name):
    users_database_manager.add_rich_client(name, password, plane_name)


def make_runway_free():
    runway = input("What runway you want to make free? ")
    runway = int(runway)

    lines_database_manager.make_runway_free(runway)


def check_for_free_runway():
    date = input("What is the date? ")
    date = str(date)
    runways = lines_database_manager.get_free_runways()

    runways_table = PrettyTable(['Number'])
    runways_table.padding_width = 1

    for runway in runways:
        if users.calculate_time_before(runway[1], date + " 23:59")\
                and users.calculate_time_after(runway[1], date + " 00:00"):
            runways_table.add_row([runway[0]])
    print(runways_table)
