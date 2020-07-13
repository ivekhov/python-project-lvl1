#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script for brain-even start."""


from brain_games.games import ask_user, constants, make_calcs, say_to_user


def main():
    """Call functions according to general logic."""
    say_to_user.make_intro(constants.WELCOME, constants.GREET_TO_EVEN)
    user_name = ask_user.ask_name()
    say_to_user.greet_user(user_name)
    counter = constants.ATTEMPTS
    while counter > 0:
        number = make_calcs.call_random()
        ask_user.ask_question(number)
        answer = ask_user.get_answer()
        correct = make_calcs.is_even(number)
        if answer == correct:
            say_to_user.say_correct()
            counter = counter - 1
        else:
            say_to_user.error_message(answer, correct, user_name)
            break
        if counter == 0:
            say_to_user.congratulate_user(user_name)


if __name__ == '__main__':
    main()
