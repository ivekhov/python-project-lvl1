# -*- coding:utf-8 -*-

"""Script for brain-gcd start."""


from brain_games.functions import ask_user, make_calcs, say_to_user


def start_game():
    """Call functions according to general logic."""
    say_to_user.make_intro(make_calcs.WELCOME, make_calcs.GREET_TO_GCD)
    user_name = ask_user.ask_name()
    say_to_user.greet_user(user_name)
    counter = make_calcs.ATTEMPTS
    while counter > 0:
        first_item = make_calcs.call_random()
        second_item = make_calcs.call_random()
        ask_user.ask_question_gcd(first_item, second_item)
        answer = ask_user.get_answer_int()
        correct = make_calcs.answer_gcd(first_item, second_item)
        if answer == correct:
            say_to_user.say_correct()
            counter = counter - 1
        else:
            say_to_user.error_message(answer, correct, user_name)
            break
        if counter == 0:
            say_to_user.congratulate_user(user_name)
