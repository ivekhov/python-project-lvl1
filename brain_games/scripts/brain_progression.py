#!/usr/bin/env python3

"""Script for brain-progression start."""


from brain_games.games import progression
from brain_games import engine


def main():
    """Call functions according to general logic."""
    engine.play(progression)


if __name__ == '__main__':
    main()
