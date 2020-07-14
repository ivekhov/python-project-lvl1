# -*- coding:utf-8 -*-

"""Logic of brain-calc game."""

from brain_games.functions import ask_user, make_calcs, say_to_user


def start_game():
    """Call functions according to game logic."""
    say_to_user.make_intro(make_calcs.WELCOME, make_calcs.GREET_TO_CALC)
    user_name = ask_user.ask_name()
    say_to_user.greet_user(user_name)
    counter = make_calcs.ATTEMPTS
    while counter > 0:
        first_item = make_calcs.call_random()
        second_item = make_calcs.call_random()
        operator = make_calcs.call_operator()
        ask_user.ask_question_calc(first_item, second_item, operator)
        answer = ask_user.get_answer_int()
        correct = make_calcs.answer_calc(first_item, second_item, operator)
        if answer == correct:
            say_to_user.say_correct()
            counter = counter - 1
        else:
            say_to_user.error_message(answer, correct, user_name)
            break
        if counter == 0:
            say_to_user.congratulate_user(user_name)
