# -*- coding:utf-8 -*-

"""Game of brain-calc."""

import prompt

from brain_games import engine

GREET = 'What is the result of the expression?'


def get_question_and_answer() -> (int, int):
    """
    Get answer from user and calculate correct answer.

    Returns:
        int: user`s answer.
        int: correct answer.
    """
    first_item = engine.call_random()
    operator = engine.call_operator()
    second_item = engine.call_random()
    if operator == '+':
        correct = first_item + second_item
    elif operator == '-':
        correct = first_item - second_item
    elif operator == '*':
        correct = first_item * second_item

    print('Question: {0} {1} {2}'.format(first_item, operator, second_item))
    answer = prompt.integer(prompt='Your answer: ')
    return answer, correct


def main():
    """Create calcs game logic."""
    engine.play_game(GREET, get_question_and_answer)
