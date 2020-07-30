# -*- coding:utf-8 -*-

"""Game of brain-calc."""

import operator
import random

import prompt

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


def get_question_and_answer() -> (int, int):
    """
    Get answer from user and calculate correct answer.

    Returns:
        int: user`s answer.
        int: correct answer.
    """
    first_item = random.randint(RANDOM_FROM, RANDOM_TO)     # noqa: S311
    operation = call_operator()
    second_item = random.randint(RANDOM_FROM, RANDOM_TO)    # noqa: S311
    if operation == '+':
        correct = operator.add(first_item, second_item)
    elif operation == '-':
        correct = operator.substract(first_item, second_item)
    elif operation == '*':
        correct = operator.mul(first_item, second_item)

    print('Question: {0} {1} {2}'.format(first_item, operation, second_item))
    answer = prompt.integer(prompt='Your answer: ')
    return answer, correct


def start_game():
    """Create calcs game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
