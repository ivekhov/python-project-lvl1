"""Contains functions and constants for building game logic."""

import prompt

ATTEMPT_COUNTS = 3


def play(game):
    """
    Create boilerplate for game.

    Args:
        game: function with particular game.
    """
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string(prompt='\nMay I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    for _ in range(0, ATTEMPT_COUNTS):
        question, correct = game.get_question_and_answer()
        print('Question: {}'.format(question))
        answer = prompt.string(prompt='Your answer: ')
        if answer != correct:
            print("'{}' is wrong answer ;(.".format(answer), end=' ')
            print("Correct answer was {}".format(correct))
            print("Let's try again, {}!".format(name))
            return
        else:
            print('Correct!')
        print('Congratulations, {}!\n'.format(name))
