# -*- coding:utf-8 -*-

"""Script for brain-prime start."""


from brain_games.functions import ask_user, make_calcs, say_to_user


def start_game():
    """Call functions according to general logic."""
    say_to_user.make_intro(make_calcs.WELCOME, make_calcs.GREET_TO_PRIME)
    user_name = ask_user.ask_name()
    say_to_user.greet_user(user_name)
    counter = make_calcs.ATTEMPTS
    while counter > 0:
        number = make_calcs.call_random()
        ask_user.ask_question(number)
        answer = ask_user.get_answer()
        correct = make_calcs.is_prime(number)
        correct = make_calcs.convert_bool_to_str(correct)
        if answer == correct:
            say_to_user.say_correct()
            counter = counter - 1
        else:
            say_to_user.error_message(answer, correct, user_name)
            break
        if counter == 0:
            say_to_user.congratulate_user(user_name)
