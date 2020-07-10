# -*- coding:utf-8 -*-

"""Make intro to game, ask user`s name greet user."""


def make_intro():
    """Welcome and say rules of game."""
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')


def greet_user(name):
    """
    Say 'Hello' to user.

    Args:
        name: user`s name from ask_name function.
    """
    print('Hello, {0}!\n'.format(name))


def congratulate_user(name):
    """
    Say 'Congratulations' to user, when he wins.

    Args:
        name: user`s name from ask_name function.
    """
    print('Congratulations, {0}!\n'.format(name))


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


def say_correct():
    """Say 'correct', if answer is right."""
    print('Correct!')
