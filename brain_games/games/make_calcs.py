# -*- coding:utf-8 -*-

"""Work with numbers in game."""


from itertools import count
from math import gcd
from random import choice, randint

from brain_games.games import constants


def call_random(start=constants.RANDOM_FROM, stop=constants.RANDOM_TO) -> int:
    """
    Return (pseudo)random integer.

    Args:
        start: first item in range, default is 1
        stop: last item in range, default is 256

    Returns:
        int
    """
    return randint(start, stop)     # noqa: S311


def is_even(number) -> str:
    """
    Check if number is even or not.

    Args:
        number: was generated by call_random function.

    Returns:
        str: 'yes' is even, 'no' is odd.
    """
    if number % 2 == 0:
        return 'yes'
    return 'no'


def call_operator(operators=constants.OPERATORS) -> str:
    """
    Return randomly selected operator.

    Args:
        operators: set of possible values. Default is 4-elems set (constants).

    Returns:
        str: operator selected from set.
    """
    return choice(operators)        # noqa: S311


def answer_calc(first_item, second_item, operator) -> int:
    """
    Return answer on arithmetical expression.

    Args:
        first_item: integer.
        second_item: integer.
        operator: str.

    Returns:
        int: result of expression.
    """
    if operator == '+':
        return first_item + second_item
    elif operator == '-':
        return first_item - second_item
    elif operator == '*':
        return first_item * second_item


def answer_gcd(first_item, second_item) -> int:
    """
    Return answer on arithmetical expression.

    Args:
        first_item: integer.
        second_item: integer.

    Returns:
        int: result of greatest common divider.
    """
    return gcd(first_item, second_item)


def call_progression(start, step, length=constants.PROGRESSION_LENGTH) -> list:
    """
    Return list of integers.

    Args:
        start: first item in range
        step: last item in range
        length: count of integers in this list

    Returns:
        list: of integers
    """
    numbers = count(start=start, step=step)
    return list(next(numbers) for _ in range(length))       # noqa: C400


def is_prime(number) -> str:
    """
    Return 'yes' or 'no', if number is prime.

    Args:
        number: integer.

    Returns:
        str: 'yes' if number is prime, 'no' if not.
    """
    start = 2
    while start < number:
        if number % start == 0:
            return 'no'
        start += 1
    return 'yes'
