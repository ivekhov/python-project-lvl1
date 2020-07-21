# -*- coding:utf-8 -*-

"""Game of brain-prime."""


import prompt

from brain_games import engine

GREET = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: user`s answer.
        str: correct answer.
    """
    number = engine.call_random()
    correct = engine.is_prime(number)
    correct = engine.convert_bool_to_str(correct)
    print('Question: {0}'.format(number))
    answer = prompt.string(prompt='Your answer: ')
    return answer, correct


def main():
    """Realize prime game logic."""
    engine.play_game(GREET, get_question_and_answer)
