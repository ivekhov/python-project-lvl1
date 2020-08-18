#!/usr/bin/env python3

"""Script for brain-calc start."""


from brain_games.games import calc
from brain_games import engine


def main():
    """Call brain-calc function with game logic."""
    engine.play_game(calc)


if __name__ == '__main__':
    main()
