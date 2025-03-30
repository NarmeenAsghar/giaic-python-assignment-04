# --------------PROGRAM STATEMENT
'''
Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.
'''

# importing module
import random 

# creating function
def dice():
#generate random numbers to rolled the dice
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print(f"Dice 1 rolled at: {dice1} ------ Dice 2 rolled at: {dice2}")
# return the result
    return dice1, dice2

# main function
def main():
    print("Rolled the dices three times!")
# for rolling dice 3 times
    for i in range(3):
        print("Roll the dice", {i + 1})
        dice() # calling function to simulate dice

# calling main function
if __name__ == "__main__":
    main()