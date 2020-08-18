"""Game of brain-progression."""


import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def get_question_and_answer() -> (str, str):
    """
    Get answer from user and calculate correct answer.

    Returns:
        str: question for user.
        str: correct answer.
    """
    start = random.randint(1, PROGRESSION_LENGTH)   # noqa: S311
    step = random.randint(1, PROGRESSION_LENGTH)    # noqa: S311
    hidden_position = random.randint(0, PROGRESSION_LENGTH - 1)     # noqa: S311
    progression = [start + i * step for i in range(PROGRESSION_LENGTH)]
    answer = str(start + step * hidden_position)
    progression[hidden_position] = '...'
    question = ' '.join(map(str, progression))
    return question, answer
