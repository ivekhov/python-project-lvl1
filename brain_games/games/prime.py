# -*- coding:utf-8 -*-

"""Game of brain-prime."""


from brain_games import engine as en


def game():
    """Create even game logic."""
    en.game(en.PRIME, en.call_random, en.answer_prime, answer_type='string')
