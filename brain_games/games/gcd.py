# -*- coding:utf-8 -*-

"""Game of brain-gcd."""


import prompt

from brain_games import engine

GREET = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer() -> (int, int):
    """
    Get answer from user and calculate correct answer.

    Returns:
        int: user`s answer.
        int: correct answer.
    """
    numbers = [engine.call_random(), engine.call_random()]
    large = max(numbers)
    small = min(numbers)
    residual = large % small
    while residual != 0:
        large = small
        small = residual
        residual = large % small
    correct = small
    print('Question: {0} {1}'.format(numbers[0], numbers[1]))
    answer = prompt.integer(prompt='Your answer: ')
    return answer, correct


def main():
    """Create gcd game logic."""
    engine.play_game(GREET, get_question_and_answer)
