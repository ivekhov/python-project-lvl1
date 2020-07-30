# -*- coding:utf-8 -*-

"""Game of brain-progression."""


import itertools
import random

from brain_games import engine

QUESTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def make_progression(start, step, length=PROGRESSION_LENGTH) -> list:
    """
    Return list of integers for progression expression.

    Args:
        start: first item in range.
        step: last item in range.
        length: count of integers in this list.

    Returns:
        list: three integer values.
    """
    numbers = itertools.count(start=start, step=step)
    return list(next(numbers) for _ in range(length))       # noqa: C400


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: question for user.
        str: correct answer.
    """
    start = random.randint(1, PROGRESSION_LENGTH)   # noqa: S311
    step = random.randint(1, PROGRESSION_LENGTH)    # noqa: S311
    hidden_position = random.randint(0, PROGRESSION_LENGTH - 1)     # noqa: S311
    progression = make_progression(start, step)
    task = [progression, hidden_position, progression[hidden_position]]
    correct = task[2]
    answer = str(correct)
    temp = task[0]
    temp[task[1]] = '..'
    row_progr = ' '.join([str(num) for num in temp])
    question = ' '.join(['Question:', row_progr])
    return question, answer


def start_game():
    """Create progression game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
