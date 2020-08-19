"""Contains functions and constants for building game logic."""

import prompt

ATTEMPTS = 3


def play_game(game):
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
    for attempt in range(0, ATTEMPTS):
        question, correct = game.get_question_and_answer()
        print('Question: {}'.format(question))
        answer = prompt.string(prompt='Your answer: ')
        if answer == correct:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(.".format(answer), end=' ')
            print("Correct answer was {}".format(correct))
            print("Let's try again, {}!".format(name))
            break
        if attempt == 2:
            print('Congratulations, {}!\n'.format(name))
