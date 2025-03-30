# ----------------PROBLEM STATEMENT:
'''
Write a function that takes a list of numbers and returns the sum of those numbers.
'''


# exp-1
# with default list
def sum_numbers(numbers):
# checks total is 0 
    total = 0
# for loop for each number in numbers
    for number in numbers:
# total = total + number (to add each number in total)
        total += number
    return total # returns the total number after addition
    
def main():
    numbers = [23, 11, 9, 16, 20]
    result = sum_numbers(numbers)
    print(f"The result of {numbers} listed numbers is {result}")

if __name__ == "__main__":
    main()


print("=" * 80)


# exp-2
# with user input list
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
    
def main():
    numbers = input("Enter numbers with spaces to sum them using list: ")
# split add input numbers into string(like: 1 2 3 4 then output= ["1", "2", "3", "4"])
# map(int, ---) used to change string into integer for correct result
    numbers = list(map(int, numbers.split()))
    result = sum_numbers(numbers)
    print(f"The result of {numbers} listed numbers is {result}")

if __name__ == "__main__":
    main()