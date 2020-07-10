# -*- coding:utf-8 -*-

"""Make intro to game, ask user`s name greet user."""


import prompt


def ask_name() -> str:
    """
    Ask user`s name.

    Returns:
        str.

    """
    return prompt.string(prompt='\nMay I have your name? ')


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
