"""Game of brain-calc."""

import operator
import random

from brain_games import engine

QUESTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')
RANDOM_FROM = 1
RANDOM_TO = 25


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: question for user.
        str: correct answer.
    """
    first = random.randint(RANDOM_FROM, RANDOM_TO)     # noqa: S311
    operation = random.choice(OPERATORS)
    second = random.randint(RANDOM_FROM, RANDOM_TO)    # noqa: S311
    if operation == '+':
        correct = operator.add(first, second)
    elif operation == '-':
        correct = operator.sub(first, second)
    elif operation == '*':
        correct = operator.mul(first, second)
    question = ' '.join(['Question:', str(first), operation, str(second)])
    return question, str(correct)


def start_game():
    """Create calcs game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
