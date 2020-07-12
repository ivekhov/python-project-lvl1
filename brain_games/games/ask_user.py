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


def ask_question_calc(first_item, second_item, operator):
    """
    Suggest an expression for calculation.

    Args:
        first_item: int (pseudo) random integer generated.
        second_item: int (pseudo) random integer generated.
        operator: str (pseudo) random selected from list of operators.
    """
    print('Question: {0} {1} {2}'.format(first_item, operator, second_item))


def ask_question_gcd(first_item, second_item):
    """
    Suggest an expression for gcd.

    Args:
        first_item: int (pseudo) random integer generated.
        second_item: int (pseudo) random integer generated.
    """
    print('Question: {0} {1}'.format(first_item, second_item))


def get_answer_int() -> int:
    """
    Get answer and return integer.

    Returns:
        int.
    """
    return prompt.integer(prompt='Your answer: ')


def ask_question_progression(progression, hidden_position):
    """
    Suggest an expression for arithmetical progression.

    Args:
        progression: list of numbers.
        hidden_position: index of element that should be hidden to user.
    """
    temp = progression
    temp[hidden_position] = '..'
    print('Question:', end=' ')
    print(*temp)
