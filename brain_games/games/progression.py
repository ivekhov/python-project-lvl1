# -*- coding:utf-8 -*-

"""Game of brain-progression."""


import prompt

from brain_games import engine

GREET = 'What number is missing in the progression?'


def get_question_and_answer() -> (int, int):
    """
    Get answer from user and calculate correct answer.

    Returns:
        int: user`s answer.
        int: correct answer.
    """
    task = engine.create_task_prog()
    correct = task[2]
    temp = task[0]
    temp[task[1]] = '..'
    print('Question:', end=' ')
    print(*temp)
    answer = prompt.integer(prompt='Your answer: ')
    return answer, correct


def main():
    """Create progression game logic."""
    engine.play_game(GREET, get_question_and_answer)
