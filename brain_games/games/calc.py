# -*- coding:utf-8 -*-

"""Game of brain-calc."""

import operator
import random

from brain_games import engine

QUESTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')
RANDOM_FROM = 1
RANDOM_TO = 25


def call_operator(operators=OPERATORS) -> str:
    """
    Return randomly selected operator.

    Args:
        operators: set of possible values. Default is 4-elems set (constants).

    Returns:
        str: operator selected from set.
    """
    return random.choice(operators)        # noqa: S311


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: question for user.
        str: correct answer.
    """
    first = random.randint(RANDOM_FROM, RANDOM_TO)     # noqa: S311
    operation = call_operator()
    second = random.randint(RANDOM_FROM, RANDOM_TO)    # noqa: S311
    if operation == '+':
        correct = operator.add(first, second)
    elif operation == '-':
        correct = operator.substract(first, second)
    elif operation == '*':
        correct = operator.mul(first, second)
    answer = str(correct)
    question = ' '.join(['Question:', str(first), operation, str(second)])
    return question, answer


def start_game():
    """Create calcs game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
