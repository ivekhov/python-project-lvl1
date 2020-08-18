"""Contains functions and constants for building game logic."""

import prompt

ATTEMPTS = 3


# def make_intro(*args):
#     """
#     Say welcome and rules of game.

#     Args:
#         *args: phrases for welcome speech.
#     """
#     for phrase in args:
#         print(phrase)


def play_game(QUESTION, get_question_and_answer):
    """
    Create boilerplate for game.

    Args:
        greet: welcome phrase per particuar game.
        get_question_and_answer: function.
    """
    print('Welcome to the Brain Games!')
    print(QUESTION)
    name = prompt.string(prompt='\nMay I have your name? ')
    print('Hello, {}!'.format(name))
    print()
    counter = ATTEMPTS
    while counter > 0:
        question, correct = get_question_and_answer()
        print(question)
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
