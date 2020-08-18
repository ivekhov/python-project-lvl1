"""Game of brain-gcd."""

import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
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


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: question for user.
        str: correct answer.
    """
    first = random.randint(RANDOM_FROM, RANDOM_TO)       # noqa: S311
    second = random.randint(RANDOM_FROM, RANDOM_TO)      # noqa: S311
    correct = find_gcd(first, second)
    question = ' '.join([str(first), str(second)])
    return question, str(correct)
