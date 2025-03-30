# ----------------PROBLEM STATEMENT:
'''
Fill out the function shorten(lst) which removes elements from the end of lst,
which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
If lst is already shorter than MAX_LENGTH you should leave it unchanged. 
We've written a main() function for you which gets a list and passes it into your function once you run the program. 
For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.
'''
# default lenght
MAX_LENGTH = 4

def shorten(lst):
# if input value's length is greater then max-length then delete(pop) last element and also print it
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        print(last_element)

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
    shorten(lst)    # print the last element

# calling function
if __name__ == "__main__":
    main()