# --------------PROGRAM STATEMENT
'''
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
'''

# importing math module
import math

def main():
# input from user (length of sides of right triangle)
    side1: float = float(input("Enter the length of side 1 (one leg of the triangle): "))
    side2: float = float(input("Enter the length of side 2 (the other leg of the triangle): "))

# calculating the hypotenuse using Pythagorean theorem
# sqrt stands for square root of numbers
    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
    print(f"The length of the hypotenuse is: {hypotenuse}")

# calling function
if __name__ == "__main__":
    main()
