# ----------------PROBLEM STATEMENT:
'''
fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list.
'''

def add_three_copies(list, data):
# add three copies of 'data' to the provided list
    for i in range(3):  # loop 3 times to add three copies
        list.append(data)  # Add the data to the list each time

def main():
# get user input
    text = input("Enter the text for copy: ")
# empty list
    list = []
    print("List before copy:", list)
# call the function to add three copies of the text to the list
    add_three_copies(list, text)
    print("List after copy:", list)
# calling function
if __name__ == "__main__":
    main()
