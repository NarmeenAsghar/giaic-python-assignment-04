# ----------------PROBLEM STATEMENT:
'''
Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
'''

def main():
# empty list
    list_input = []
# user input the value
    value = input("Enter the value: ")
# while loop keep executing as long as the condition of value is not as empty string
    while value:
# adds values in list
        list_input.append(value)
# input for other with loop
        value = input("Enter the value: ")
# if user press enter without giving value loop will stop and this print statement will run
    print("Here is the list:", list_input)
# calling function
if __name__ == '__main__':
    main()