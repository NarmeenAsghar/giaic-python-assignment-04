#-------PROGRAM STATEMENT:
'''
Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
'''

# for fahernheit
# creating function
def main():
    celsius = float(input("Enter the temperature in celsius to change it in fahrenheit: "))
# using the formula of fahernheit to change the celsius
    fahrenheit = 9/5 * celsius + 32

    print(f"The temperature in {celsius} °C is equals to {fahrenheit} °F")

# calling function
if __name__ == "__main__":
    main()


print("=" * 100)


# for celsius
# creating function
def main():
    fahrenheit = float(input("Enter the temperature in fahrenheit to change it in celsius: "))
# using the formula of celsius to change the fahernheit
    celsius = 5/9 * fahrenheit + 32

    print(f"The temperature in {fahrenheit} °F is equals to {celsius} °C")

# calling function
if __name__ == "__main__":
    main()