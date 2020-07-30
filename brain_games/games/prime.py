# -*- coding:utf-8 -*-

"""Game of brain-prime."""


import prompt

from brain_games import engine

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number) -> bool:
    """
    Check, if number is prime.

    Args:
        number: integer.

    Returns:
        bool: True if number is prime, False if not.
    """
    if number <= 1:
        return False
    start = 2
    while start < number // 2 + 1:
        if number % start == 0:
            return False
        start += 1
    return True


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
    correct = is_prime(number)
    correct = convert_bool_to_str(correct)
    print('Question: {0}'.format(number))
    answer = prompt.string(prompt='Your answer: ')
    return answer, correct


def start_game():
    """Realize prime game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
