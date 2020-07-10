# -*- coding:utf-8 -*-

"""Make intro to game, ask user`s name greet user."""


import prompt


def make_intro():
    """Welcome and say rules of game."""
    print('\nWelcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no"')


def ask_name() -> str:
    """
    Ask user`s name.

    Returns:
        str.

    """
    return prompt.string(prompt='\nMay I have your name? ')


def greet_user(name):
    """
    Say 'Hello' to user.

    Args:
        name: user`s name from ask_name function.
    """
    print('Hello, {0}!\n'.format(name))


def ask_question(number):
    """
    Suggest user a number for evaluation.

    Args:
        number: (pseudo)random integer generated.
    """
    print('Question: {0}'.format(number))


def get_answer() -> str:
    """
    Get answer and return string.

    Returns:
        str.
    """
    return prompt.string(prompt='Your answer: ')


def congratulate_user(name):
    """
    Say 'Congratulations' to user, when he wins.

    Args:
        name: user`s name from ask_name function.
    """
    print('Congratulations, {0}!\n'.format(name))


def error_message(answer, correct, name):
    """
    Print correct answer and say goodbye.

    Args:
        answer: str
        correct: str
        name: str

    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.")
    print("Let's try again, {0}!".format(name))
