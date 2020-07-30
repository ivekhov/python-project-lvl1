# -*- coding:utf-8 -*-

"""Game of brain-gcd."""

import random

import prompt

from brain_games import engine

QUESTION = 'Find the greatest common divisor of given numbers.'
RANDOM_FROM = 1
RANDOM_TO = 25


def find_gcd(first, second) -> int:
    """
    Find greatest common dividet of two given numbers.

    Args:
        first: int.
        second: int.

    Returns:
        int: gcd of two numbers.
    """
    if first > second:
        large, small = first, second
    else:
        large, small = second, first
    residual = large % small
    while residual != 0:
        large = small
        small = residual
        residual = large % small
    return small


def get_question_and_answer() -> (int, int):
    """
    Get answer from user and calculate correct answer.

    Returns:
        int: user`s answer.
        int: correct answer.
    """
    numbers = [random.randint(RANDOM_FROM, RANDOM_TO), random.randint(RANDOM_FROM, RANDOM_TO)]      # noqa: S311, E501
    correct = find_gcd(numbers[0], numbers[1])
    print('Question: {0} {1}'.format(numbers[0], numbers[1]))
    answer = prompt.integer(prompt='Your answer: ')
    return answer, correct


def start_game():
    """Create gcd game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
