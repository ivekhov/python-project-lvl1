# -*- coding:utf-8 -*-

"""Game of brain-even."""


import prompt

from brain_games import engine

QUESTION = 'Answer "yes" if number even otherwise answer "no".'


def is_even(number) -> bool:
    """
    Check, if number is even or not.

    Args:
        number: was generated by call_random function.

    Returns:
        bool: True is even, False is odd.
    """
    return not number % 2


def convert_bool_to_str(answer) -> str:
    """
    Convert True into 'yes', False into 'no'.

    Args:
        answer: bool.

    Returns:
        str: 'yes' or 'no'.
    """
    if answer is True:
        return 'yes'
    return 'no'


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: user`s answer.
        str: correct answer.
    """
    number = engine.call_random()
    correct = is_even(number)
    correct = convert_bool_to_str(correct)
    print('Question: {0}'.format(number))
    answer = prompt.string(prompt='Your answer: ')
    return answer, correct


def start_game():
    """Make game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
