# -*- coding:utf-8 -*-

"""Game of brain-progression."""


from brain_games import engine as en


def game():
    """Create progression game logic."""
    en.game(en.GREET_TO_PROG, en.create_task_prog, en.answer_prog, is_prog=True)
