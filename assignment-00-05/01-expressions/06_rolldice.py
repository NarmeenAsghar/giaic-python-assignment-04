# --------------PROGRAM STATEMENT
'''
Simulate rolling two dice, and prints results of each roll as well as the total.
'''

# import for random numbers
import random
# constant die number
no_of_dice: int = 6

def main():
# random numbers of die
    dice1: int = random.randint(1, no_of_dice)
    dice2: int = random.randint(1, no_of_dice)
# total of both dice
    total: int = dice1 + dice2

    print("Rolled First Die =", dice1)
    print("Rolled Second Die =", dice2)
    print("=================Total of both dice:", total)

# calling function
if __name__ == '__main__':
    main()