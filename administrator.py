import users
import users_database_manager
import lines_database_manager


def show_admin_options(username):
    while True:
        show_options()

        choice = input("Make your choice: ")
        choice = int(choice)
        if choice == 1:
            users.show_flight_list()
        elif choice == 2:
            users.show_seats_scheme()
        elif choice == 3:
            sell_ticket(username)
        elif choice == 4:
            users.show_free_runways()
        elif choice == 5:
            give_permission()
        elif choice == 6:
            check_passenger()
        elif choice == 7:
            break
        else:
            print("\nWrong number!")


def show_options():
    print("\nTo see flights press 1")
    print("To see seats for a flight press 2")
    print("To sell a ticket press 3")
    print("To check runway press 4")
    print("To give permssion for using runway press 5")
    print("To check passenger's ticket press 6")
    print("To logout press 7")


def sell_ticket(username):
    ticket = users.settng_ticket_sold_procedure(username)
    if len(ticket) == 0:
        print("This ticket is already taken. Pick anothe one. \
            For more information look at the seats table.")


def check_passenger():
    ticket_id = input("\nNumber Of ticket: ")
    ticket_id = (ticket_id)
    user = input("Username: ")
    user = (user)

    if users_database_manager.check_ticket(ticket_id, user):
        print("\nThis passenger is OK!")
    else:
        print("\nCALL THE POLICE")


def give_permission():
    runway_number = input("Number Of runway: ")
    runway_number = int(runway_number)
    time = input("Time (Dont forget the template (DD-MM-YY HH:MM)): ")
    time = str(time)
    runway = lines_database_manager.get_runway(runway_number)
    if runway[0] == 1:
        if users.calculate_time_before(time, runway[1]):
            print("\nGO :)")
            lines_database_manager.set_permission_given_at_time(
                runway_number, time)
        else:
            print("\nPermission DENIED :(")
            print("This runway is taken! Try with other time!")
    else:
        print("\nPermission DENIED :(")
        print("This runway is already taken! Try with other!")


def register_if_possible(username, password):
    master_code = input("\nEnter master code: ")
    master_code = int(master_code)
    if check_master_code(master_code) and users.is_not_duplicated(username):
        register(username, password)
        return True
    return False


def check_master_code(master_code):
    return users_database_manager.check_code(master_code)


def register(name, password):
    users_database_manager.add_administrator(name, password)
