#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""Script for brain-even start."""


from brain_games import ask_user, make_calcs, say_to_user


def main():
    """Call functions according to general logic."""
    say_to_user.make_intro()
    user_name = ask_user.ask_name()
    say_to_user.greet_user(user_name)
    counter = 3
    while counter > 0:
        number = make_calcs.call_random()
        ask_user.ask_question(number)
        answer = ask_user.get_answer()
        if make_calcs.is_even(number) is make_calcs.is_answer_even(answer):
            say_to_user.say_correct()
            counter = counter - 1
        else:
            correct = make_calcs.correct_answer(number)
            say_to_user.error_message(answer, correct, user_name)
            break
        say_to_user.congratulate_user(user_name)


if __name__ == '__main__':
    main()
