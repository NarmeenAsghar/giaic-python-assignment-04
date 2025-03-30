# ----------------PROBLEM STATEMENT:
'''
Write a program that doubles each element in a list of numbers.
'''

# exp-1
# with default list
def main():
    numbers: list[int] = [2, 3, 5, 10]
# len used to check the length of listed numbers
# double each element in the list and update it at the same position
    for i in range(len(numbers)):
        numbers[i] *= 2

    print(f"The double of [2, 3, 5, 10] is {numbers}")

if __name__ == "__main__":
    main()


print("=" * 80)


# exp-2
# with input list method
def main():
    numbers = input("Enter the numbers with spaces: ")
# split add input numbers into string(like: 1 2 3 4 then output= ["1", "2", "3", "4"])
# map(int, ---) used to change string into integer for correct result
    numbers = list(map(int, numbers.split()))
# len used to check the length of listed numbers
# double each element in the list and update it at the same position
    for i in range(len(numbers)):
        numbers[i] *= 2

    print(f"The double of your input numbers is {numbers}")

if __name__ == "__main__":
    main()