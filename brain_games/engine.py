# -*- coding:utf-8 -*-

"""Contains functions and constants for building game logic."""

import prompt

ATTEMPTS = 3
WELCOME = '\nWelcome to the Brain Games!'


def make_intro(*args):
    """
    Say welcome and rules of game.

    Args:
        *args: phrases for welcome speech.
    """
    for phrase in args:
        print(phrase)


def error_message(an, cr, name):
    """
    Print correct answer and say goodbye.

    Args:
        an: str - answer from user
        cr: str - correct answer from user
        name: str - user name

    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(an, cr))
    print("Let's try again, {0}!".format(name))


def play_game(greet, get_question_and_answer):
    """
    Create boilerplate for game.

    Args:
        greet: welcome phrase per particuar game.
        get_question_and_answer: function.
    """
    make_intro(greet)
    user_name = prompt.string(prompt='\nMay I have your name? ')
    print('Hello, {0}!\n'.format(user_name))
    counter = ATTEMPTS
    while counter > 0:
        answer, correct = get_question_and_answer()
        if answer == correct:
            print('Correct!')
            counter = counter - 1
        else:
            error_message(answer, correct, user_name)
            break
        if counter == 0:
            print('Congratulations, {0}!\n'.format(user_name))
