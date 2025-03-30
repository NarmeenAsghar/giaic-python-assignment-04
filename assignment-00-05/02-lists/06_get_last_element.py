# ----------------PROBLEM STATEMENT:
'''
Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
'''

# prints last elemwnt of list
def get_last_element(lst):
    """Prints the last element of the list."""
    print(lst[-1])

def get_lst():
    lst = []
    element = input("Enter an element of the list or press enter to stop: ")
# means it will stop the process when user press enter without giving any input
    while element != "":
# add elements to the list
        lst.append(element)
        element = input("Enter an element of the list or press enter to stop: ")
    return lst # return filled list

def main():
    lst = get_lst()    # get the prints from the user
    get_last_element(lst)    # print the last element

# calling function
if __name__ == "__main__":
    main()