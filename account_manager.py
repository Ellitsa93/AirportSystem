import users
import rich_client
import administrator
import passenger
import users_database_manager
import lines_database_manager


def main():
    print("WELCOME!")
    print("This is EllitsaAirlines!")
    while True:
        print("\nTo log in press 1")
        print("To register press 2")
        print("To exit press 3")
        choice = input("What do you want to do? ")
        choice = int(choice)
        if choice == 1:
            login()
        elif choice == 2:
            register()
        elif choice == 3:
            break
        else:
            print("\nWrong number!")


def login():
    name = input("Username: ")
    name = str(name)
    password = input("Password: ")
    password = str(password)
    if users.check_category(name, password) == 1:
        administrator.show_admin_options(name)
    elif users.check_category(name, password) == 2:
        passenger.show_passenger_options(name)
    elif users.check_category(name, password) == 3:
        rich_client.show_rich_client_options(name)
    else:
        print("\nWrong name ot password!")


def define_regisration_type():
    print("\nOK now what type of user are you??")
    print("For administrator press 1")
    print("For passenger press 2")
    print("For rich client press 3")
    print("To exit press 4")
    choice = input("Take your choice and be honest! ")
    choice = int(choice)

    return choice


def register():
    choice = define_regisration_type()

    name = input("Enter name: ")
    name = str(name)
    password = input("Enter password: ")
    password = str(password)

    if choice == 1:
        if administrator.register_if_possible(name, password):
            print("""\nSuccessfully registered administrator with
                name {0} and password {1}""".format(name, password))
    elif choice == 2:
        if passenger.register_if_possible(name, password):
            print("""\nYou were successfully regitered in the system :)
            Check your email for security code""")
    elif choice == 3:
        if rich_client.register_if_possible(name, password):
            print("\nYou were successfully regitered in the system")
    else:
        print("\nWrong number!")

if __name__ == '__main__':
    main()
