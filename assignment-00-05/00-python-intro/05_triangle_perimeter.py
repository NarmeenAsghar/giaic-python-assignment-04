#-------PROGRAM STATEMENT:
'''
Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle 
'''

# exp-1
# simple python code
side1 = float(input("What is the length of 1st side of triangle? "))
side2 = float(input("What is the length of 2nd side of triangle? "))
side3 = float(input("What is the length of 3rd side of triangle? "))

perimeter = side1 + side2 + side3
print("The perimeter of triangle is ", perimeter)


print("-" * 80)


# exp-2
# creating function
def main():
    ques1 = "What is the length of 1st side of triangle?"
    print(ques1)
    side1 = float(input("Enter the 1st length: "))

    ques2 = "What is the length of 2nd side of triangle?"
    print(ques2)
    side2 = float(input("Enter the 2nd length: "))

    ques3 = "What is the length of 3rd side of triangle?"
    print(ques3)
    side3 = float(input("Enter the 3rd length: "))

    print("The perimeter of triangle is " + str(side1 + side2 + side3))


# calling function
if __name__ == "__main__":
    main()
