#!/usr/bin/env python3

"""Script for brain-gcd start."""


from brain_games.games import gcd
from brain_games import engine


def main():
    """Call functions according to general logic."""
    engine.play(gcd)


if __name__ == '__main__':
    main()
