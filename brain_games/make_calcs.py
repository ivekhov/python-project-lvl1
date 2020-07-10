# -*- coding:utf-8 -*-

"""Work with numbers in game."""


from random import randint


def call_random(start=1, stop=256) -> int:
    """
    Return (pseudo)random integer.

    Args:
        start: first item in range, default is 1
        stop: last item in range, default is 256

    Returns:
        int
    """
    return randint(start, stop)     # noqa: S311


def is_even(number) -> bool:
    """
    Return true if number is even, return false if not (i.e. is odd).

    Args:
        number: was generated by call_random function.

    Returns:
        bool.
    """
    return number % 2 == 0


def is_answer_even(answer) -> bool:
    """
    Return True if answer is 'yes', False if answer is 'not'. Else return None.

    Args:
        answer: from user.

    Returns:
        bool.
    """
    if answer == 'yes':
        return True
    elif answer == 'no':
        return False
    return None


def correct_answer(number) -> str:
    """
    Return str name of correct answer.

    Args:
        number: int.

    Returns:
        str.
    """
    if is_even(number):
        return 'yes'
    return 'no'
