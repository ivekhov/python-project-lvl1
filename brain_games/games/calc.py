# -*- coding:utf-8 -*-

"""Game of brain-calc."""


from brain_games import engine as en


def game():
    """Create calcs game logic."""
    en.game(en.GREET_TO_CALC, en.create_task_calc, en.answer_calc)
