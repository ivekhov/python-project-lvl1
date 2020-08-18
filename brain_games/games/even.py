"""Game of brain-even."""

import random

from brain_games import engine

QUESTION = 'Answer "yes" if number even otherwise answer "no".'
RANDOM_FROM = 1
RANDOM_TO = 25


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: question for user.
        str: correct answer.
    """
    number = random.randint(RANDOM_FROM, RANDOM_TO)     # noqa: S311
    answer = 'yes' if number % 2 == 0 else 'no'
    question = ' '.join(['Question:', str(number)])
    return question, answer


def start_game():
    """Make game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
