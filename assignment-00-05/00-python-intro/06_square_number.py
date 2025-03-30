#-------PROGRAM STATEMENT:
'''
Ask the user for a number and print its square (the product of the number times itself)
'''

# exp-1
# creating function
def main():
    number = float(input("Enter the number to see its square: "))
# exponentional power used to squared the number
    squared_num = number ** 2
    print("The squared number is ", squared_num)

# calling function
if __name__ == "__main__":
    main()


print("-" * 80)


# exp-2
# simple python code
question = "Do you want to square any number?"
print(question)

number = float(input("Enter the number to see its square: "))

squared_num = number ** 2
print("The squared number is ", squared_num)