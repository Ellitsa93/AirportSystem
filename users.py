import users_database_manager
import lines_database_manager
from prettytable import PrettyTable
from datetime import datetime


def add_extras(extras_prices):
    headphones = input("""Do you want headphones for {0} (Press 'y' or
        'n')""".format(extras_prices[0],))
    headphones = str(headphones)
    champagne = input("""Do you want champagne for {0} (Press
        'y' or 'n')""".format(extras_prices[1]))
    champagne = str(champagne)
    food = input("Do you want food for {0} (Press 'y' or 'n')".format(
        extras_prices[2]))
    food = str(food)
    return [headphones, champagne, food]


def show_flight_list():
    start_date = input("Start Date (Don't forget template DD-MM-YY HH:MM): ")
    start_date = str(start_date)
    end_date = input("End Date (Don't forget template DD-MM-YY HH:MM): ")
    end_date = str(end_date)
    destination = input("Destination: ")
    destination = str(destination)

    flights = lines_database_manager.get_flights(destination)
    flights_table = PrettyTable(['Number', 'Destination', 'Time'])
    flights_table.padding_width = 1

    for flight in flights:
        if calculate_time_before(flight[2], end_date)\
                and calculate_time_after(flight[2], start_date):
            flights_table.add_row(flight)
    print(flights_table)


def calculate_time_before(wanted_time, avaliable_time):
    wanted_day_and_time = datetime.strptime(wanted_time, "%d-%b-%Y %H:%M")
    avaliable_day_and_time = datetime.strptime(
        avaliable_time, "%d-%b-%Y %H:%M")
    day_and_time_now = datetime.now()
    if wanted_day_and_time <= avaliable_day_and_time and wanted_day_and_time\
            >= day_and_time_now:
        return True
    return False


def calculate_time_after(wanted_time, avaliable_time):
    wanted_day_and_time = datetime.strptime(wanted_time, "%d-%b-%Y %H:%M")
    avaliable_day_and_time = datetime.strptime(
        avaliable_time, "%d-%b-%Y %H:%M")
    if wanted_day_and_time >= avaliable_day_and_time:
        return True
    return False


def show_seats_scheme():
    flight_number = input("Flight Number: ")
    flight_number = int(flight_number)
    seats = lines_database_manager.get_seats(flight_number)
    seats_list = create_seats_list(seats)

    seats_table = PrettyTable(['First Column',
                               'Second Column',
                               'Corridor',
                               'Third Column',
                               'Forth Column'])

    seats_table.padding_width = 1
    for seats_rows in seats_list:
        seats_table.add_row(seats_rows)
    print(seats_table)


def create_seats_list(seats):
    seats_list = list()
    i = 0
    while i < len(seats):
        first_element = create_seat_for_showing(seats[i])
        if i+1 >= len(seats):
            second_element = ""
        else:
            second_element = create_seat_for_showing(seats[i+1])
        if i+2 >= len(seats):
            third_element = ""
        else:
            third_element = create_seat_for_showing(seats[i+2])
        if i+3 >= len(seats):
            fourth_element = ""
        else:
            fourth_element = create_seat_for_showing(seats[i+3])
        seats_list.append([first_element, second_element, "", third_element,
                           fourth_element])
        i += 4
    return seats_list


def create_seat_for_showing(seat):
    if(seat[1] == 0):
        text = str(seat[0])
    else:
        text = "X"
    return text


def show_free_runways():
    runways = lines_database_manager.get_free_runways()
    runways_table = PrettyTable(['Runway Number', 'Is free for'])
    runways_table.padding_width = 1

    for runway in runways:
        runways_table.add_row(runway)
    print(runways_table)


def check_category(username, password):
    account = users_database_manager.get_admin(username)
    if account is not None:
        return 1
    account = users_database_manager.get_passenger(username)
    if account is not None:
        return 2
    account = users_database_manager.get_rich_client(username)
    if account is not None:
        return 3
    return 4


def is_not_duplicated(username):
    duplicate_admins = users_database_manager.get_admin(username)
    duplicate_passengers = users_database_manager.get_passenger(username)
    duplicate_rich_client = users_database_manager.get_rich_client(username)
    if duplicate_admins is None and duplicate_passengers is None and\
            duplicate_rich_client is None:
        return True
    return False


def calculate_ticket_price(headphones, champagne, food, flight, seat,
                           extras_prices):
    price = 0
    if headphones == 'y':
        headphones = 1
        price += extras_prices[0]
    else:
        headphones = 0
    if champagne == 'y':
        champagne = 1
        price += extras_prices[1]
    else:
        champagne = 0
    if food == 'y':
        food = 1
        price += extras_prices[2]
    else:
        food = 0
    lines_database_manager.set_extras_to_seat(
        flight, seat, headphones, champagne, food)
    price += lines_database_manager.get_seat_price(flight, seat)
    return price


def get_price_with_promo_code(price, promo_code):
    if lines_database_manager.is_promo_code_correct(promo_code):
        percent = lines_database_manager.get_promo_code_percent(promo_code)
        saved = (percent/100)*price
        price = price - saved
        print("You just saved {0}!".format(saved))
    else:
        print("This promo code is not real! Check again!")
    return price


def settng_ticket_sold_procedure(username):
    flight = input("Number Of flight: ")
    flight = int(flight)
    seat = input("Number Of seat: ")
    seat = int(seat)

    if not lines_database_manager.is_ticket_taken(flight, seat):
        extras_prices = lines_database_manager.get_extras_prices(flight, seat)

        if extras_prices is not None and len(extras_prices) is not 0:
            extras = add_extras(extras_prices)
            price = calculate_ticket_price(
                extras[0], extras[1], extras[2], flight, seat, extras_prices)
        else:
            price = lines_database_manager.get_seat_price(flight, seat)

        price = set_promo_code(price)
        print("Ticket for " + str(price) + " SOLD!")

        ticket_id = lines_database_manager.set_seat_sold(flight, seat)
        users_database_manager.add_user_ticket(username, ticket_id)

        return [flight, seat, price]
    return list()


def set_promo_code(price):
    promo_code = input("Promo code? (y or n): ")
    promo_code = str(promo_code)
    if promo_code == 'y':
        promo_code = input("Enter your Promo code: ")
        promo_code = int(promo_code)
        price = get_price_with_promo_code(price, promo_code)
    return price
