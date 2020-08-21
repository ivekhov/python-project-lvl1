"""Game of brain-even."""

import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
RANDOM_FROM = 1
RANDOM_TO = 25


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: question for user.
        str: correct answer.
    """
    number = random.randint(RANDOM_FROM, RANDOM_TO)
    answer = 'yes' if number % 2 == 0 else 'no'
    return number, answer
