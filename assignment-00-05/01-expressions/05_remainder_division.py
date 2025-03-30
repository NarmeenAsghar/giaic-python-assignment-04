# --------------PROGRAM STATEMENT
'''
Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
'''

def main():
    print("===============Let's Divide the numbers!=============")
# input values from users 
    value1: int = int(input("Enter the first value: "))
    value2: int = int(input("Enter the second value: "))
# integer division (quotient)
    divide = value1 // value2
# modulo operation (remainder)
    reminder = value1 % value2
# output
    print(f"The division of numbers is {divide} with reminder of {reminder}")

# calling function
if __name__ == "__main__":
    main()