#!/usr/bin/env python3

"""Script for brain-even start."""


from brain_games.games import even
from brain_games import engine


def main():
    """Call even game."""
    engine.play(even)


if __name__ == '__main__':
    main()
