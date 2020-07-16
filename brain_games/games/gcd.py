# -*- coding:utf-8 -*-

"""Game of brain-gcd."""


from brain_games import engine as en


def game():
    """Create gcd game logic."""
    en.game(en.GREET_TO_GCD, en.create_task_gcd, en.answer_gcd)
