import users_database_manager
import lines_database_manager
import users
import destination_quiz
import re
import smtplib

system_email = "edsoftteamfmi@gmail.com"
system_password = "belmbelm"
subject = "Just bought ticket"
port = 587


def show_passenger_options(username):
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
            propose_destination(username)
        elif choice == 5:
            start_destination_quiz(username)
        elif choice == 6:
            break
        else:
            print("\nWrong number!")


def show_options():
    print("\nTo see flights press 1")
    print("To see seats for a flight press 2")
    print("To buy a ticket press 3")
    print("For proposing destination press 4")
    print("To start Destination Quiz press 5")
    print("To logout press 6")


def get_ticket(username):
    ticket = users.settng_ticket_sold_procedure(username)
    if len(ticket) == 0:
        print("This ticket is already taken. Pick anothe one. \
            For more information look at the seats table.")
    else:
        destination = lines_database_manager.get_destination(ticket[0])
        users_database_manager.increase_user_destination(username, destination)
        send_ticket_mail(ticket, username)


def send_ticket_mail(ticket, username):
    email = users_database_manager.get_email(username)
    email_text = """Hey :)
                    You just bought ticket for flight {0} seat {1}
                    and you spent only {2}!!""".format(ticket[0], ticket[1],
                                                       ticket[2])
    server = smtplib.SMTP('smtp.gmail.com', port)
    server.ehlo()
    server.starttls()
    server.login(system_email, system_password)
    email_body = '\r\n'.join(['To: %s' % email,
                              'From: %s' % system_email,
                              'Subject: %s' % subject,
                              '', email_text])

    server.sendmail(system_email, [email], email_body)


def propose_destination(username):
    destination = users_database_manager.get_best_destination(username)
    if destination == "":
        print("No Suggestions")
    else:
        print("You can go to {0}".format(destination))


def start_destination_quiz(username):
    destination_quiz.play(username)


def register_if_possible(name, password):
    email = input("Enter email: ")
    email = str(email)
    if users.is_not_duplicated(name):
        if is_email_valid(email):
            register(name, password, email)
        else:
            print("This is not a valid email")
    else:
        print("There is user with this name in the system. Try another one!")


def is_email_valid(email):
    rex = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"
    if re.match(rex, email) != None:
        return True
    return False


def register(name, password, email):
    users_database_manager.add_passenger(name, password, email)
