from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

def roll_dice(num_rolls, dice=make_test_dice(4, 1, 2, 6)):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    score = 0
    while num_rolls > 0:
        roll = dice()
        if roll == 1:
            roll = dice()
            return 1
        else:
            score += roll
            num_rolls -= 1
    return score
    # END PROBLEM 1

print(roll_dice(3))
print(roll_dice(1))