# -*- coding:utf-8 -*-

"""Game of brain-even."""


from brain_games import engine as en


def game():
    """Create even game logic."""
    en.game(en.GREET_TO_EVEN, en.call_random, en.answer_even, 'string')
