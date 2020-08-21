#!/usr/bin/env python3

"""Script for brain-prime start."""


from brain_games.games import prime
from brain_games import engine


def main():
    """Call functions according to general logic."""
    engine.play(prime)


if __name__ == '__main__':
    main()
