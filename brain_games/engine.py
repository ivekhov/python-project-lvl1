# -*- coding:utf-8 -*-

"""Contains functions and constants for building game logic."""


from itertools import count
from random import choice, randint

import prompt

ATTEMPTS = 3
OPERATORS = ('+', '-', '*')
RANDOM_FROM = 1
RANDOM_TO = 25
PROGRESSION_LENGTH = 10
WELCOME = '\nWelcome to the Brain Games!'


def call_random(start=RANDOM_FROM, stop=RANDOM_TO) -> int:
    """
    Return (pseudo)random integer.

    Args:
        start: first item in range, default is 1
        stop: last item in range, default is 256

    Returns:
        int
    """
    return randint(start, stop)     # noqa: S311


def call_operator(operators=OPERATORS) -> str:
    """
    Return randomly selected operator.

    Args:
        operators: set of possible values. Default is 4-elems set (constants).

    Returns:
        str: operator selected from set.
    """
    return choice(operators)        # noqa: S311


def convert_bool_to_str(answer) -> str:
    """
    Convert True into 'yes', False into 'no'.

    Args:
        answer: bool.

    Returns:
        str: 'yes' or 'no'.
    """
    if answer is True:
        return 'yes'
    return 'no'


def make_intro(*args):
    """
    Say welcome and rules of game.

    Args:
        *args: phrases for welcome speech.
    """
    for phrase in args:
        print(phrase)


def error_message(an, cr, name):
    """
    Print correct answer and say goodbye.

    Args:
        an: str - answer from user
        cr: str - correct answer from user
        name: str - user name

    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(an, cr))
    print("Let's try again, {0}!".format(name))


def call_progression(start, step, length=PROGRESSION_LENGTH) -> list:
    """
    Return list of integers for progression expression.

    Args:
        start: first item in range.
        step: last item in range.
        length: count of integers in this list.

    Returns:
        list: three integer values.
    """
    numbers = count(start=start, step=step)
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
    start = call_random(1, 10)
    step = call_random(1, 10)
    hidden_position = call_random(0, 9)
    progression = call_progression(start, step)
    return [progression, hidden_position, progression[hidden_position]]


def play_game(greet, get_question_and_answer):
    """
    Create boilerplate for game.

    Args:
        greet: welcome phrase per particuar game.
        get_question_and_answer: function.
    """
    make_intro(greet)
    user_name = prompt.string(prompt='\nMay I have your name? ')
    print('Hello, {0}!\n'.format(user_name))
    counter = ATTEMPTS
    while counter > 0:
        answer, correct = get_question_and_answer()
        if answer == correct:
            print('Correct!')
            counter = counter - 1
        else:
            error_message(answer, correct, user_name)
            break
        if counter == 0:
            print('Congratulations, {0}!\n'.format(user_name))