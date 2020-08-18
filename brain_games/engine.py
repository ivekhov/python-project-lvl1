"""Contains functions and constants for building game logic."""

import prompt

ATTEMPTS = 3


def play_game(game):
    """
    Create boilerplate for game.

    Args:
        greet: welcome phrase per particuar game.
        get_question_and_answer: function.
    """
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string(prompt='\nMay I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    counter = ATTEMPTS
    while counter > 0:
        question, correct = game.get_question_and_answer()
        print('Question: {}'.format(question))
        answer = prompt.string(prompt='Your answer: ')
        if answer == correct:
            print('Correct!')
            counter = counter - 1
        else:
            print("'{}' is wrong answer ;(.".format(answer), end=' ')
            print("Correct answer was {}".format(correct))
            print("Let's try again, {}!".format(name))
            break
        if counter == 0:
            print('Congratulations, {0}!\n'.format(name))
