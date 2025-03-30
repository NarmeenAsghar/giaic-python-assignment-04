#-------PROGRAM STATEMENT:
'''
Write a Python program that takes two integer inputs from the user and calculates their sum
'''

# creates a function to add numbers
def main():
# message for user that program is about to execute
    print("Executing the program to add two numbers")
# prompt for user to input first number
    value1: str = input("Enter the first number: ")
    number1 = int(value1) # change it into integer
# prompt for user to input second number
    value2: str = input("Enter the second value: ")
    number2 = int(value2) # change it into integer
# calculation to add numbers
    add = number1 + number2
    print("The addition of numbers is: ", add) # display

# calling function
if __name__ == "__main__":
    main()