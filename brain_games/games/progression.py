# -*- coding:utf-8 -*-

"""Game of brain-progression."""


import itertools

import prompt

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


def create_task_prog() -> list:
    """
    Create components for progression task.

    Returns:
        list:
            list with progression sequence,
            index of hidden element,
            hidden value (task for user).
    """
    start = engine.call_random(1, 10)
    step = engine.call_random(1, 10)
    hidden_position = engine.call_random(0, 9)
    progression = make_progression(start, step)
    return [progression, hidden_position, progression[hidden_position]]


def get_question_and_answer() -> (int, int):
    """
    Get answer from user and calculate correct answer.

    Returns:
        int: user`s answer.
        int: correct answer.
    """
    task = create_task_prog()
    correct = task[2]
    temp = task[0]
    temp[task[1]] = '..'
    print('Question:', end=' ')
    print(*temp)
    answer = prompt.integer(prompt='Your answer: ')
    return answer, correct


def start_game():
    """Create progression game logic."""
    engine.play_game(QUESTION, get_question_and_answer)
