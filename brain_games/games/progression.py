# -*- coding:utf-8 -*-

"""Script for brain-progression start."""


from brain_games.functions import ask_user, make_calcs, say_to_user


def start_game():
    """Call functions according to general logic."""
    say_to_user.make_intro(make_calcs.WELCOME, make_calcs.GREET_TO_PROGRESSION)
    user_name = ask_user.ask_name()
    say_to_user.greet_user(user_name)
    counter = make_calcs.ATTEMPTS
    while counter > 0:
        start = make_calcs.call_random(1, 10)
        step = make_calcs.call_random(1, 10)
        hidden_position = make_calcs.call_random(0, 9)
        progression = make_calcs.call_progression(start, step)
        correct = progression[hidden_position]
        ask_user.ask_question_progression(progression, hidden_position)
        answer = ask_user.get_answer_int()
        if answer == correct:
            say_to_user.say_correct()
            counter = counter - 1
        else:
            say_to_user.error_message(answer, correct, user_name)
            break
        if counter == 0:
            say_to_user.congratulate_user(user_name)
