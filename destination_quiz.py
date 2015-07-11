import destination_quiz_database_manager


def play(username):
    print("\nHello! This is Destination quiz!")
    while True:
        print("\nTo start quiz press 1")
        print("To quit press 2")
        choice = input("Insert the number you would like to go to: ")
        choice = int(choice)
        if choice == 1:
            if destination_quiz_database_manager.is_not_registered(username):
                destination_quiz_database_manager.add_user(username)
            new_question(username)
        elif choice == 2:
            break
        else:
            print("\nWrong number!")


def check_answer(given, right):
    if right == 1 and given == "A":
        return True
    if right == 2 and given == "B":
        return True
    if right == 3 and given == "C":
        return True
    return False


def new_question(username):
    if is_new_question_avaliable(username):
        question_and_answers = destination_quiz_database_manager.get_question(
            username)
        print_question_and_answers(question_and_answers)

        answer = input("And the right answer is (press A, B, C or D): ")
        answer = answer
        if check_answer(answer, question_and_answers[4]):
            print("\nCorrect! :)\n")
            destination_quiz_database_manager.next_question(username, True)
        else:
            print("\nIncorrect! :(\n")
            destination_quiz_database_manager.next_question(username, False)
    else:
        show_end_of_the_game_message(username)


def print_question_and_answers(question_and_answers):
    print(question_and_answers[0])
    print("A) " + question_and_answers[1])
    print("B) " + question_and_answers[2])
    print("C) " + question_and_answers[3])


def show_end_of_the_game_message(username):
    all_answers = destination_quiz_database_manager.get_questions_count()
    rights_answers = all_answers - \
        destination_quiz_database_manager.get_number_of_wrong_answers(
            username)
    print("You finished the game!")
    print("Your score is {0}".format(rights_answers/all_answers))


def is_new_question_avaliable(username):
    all_questions = destination_quiz_database_manager.get_questions_count()
    answered = destination_quiz_database_manager.get_last_answered(username)
    if answered <= all_questions:
        return True
    return False
