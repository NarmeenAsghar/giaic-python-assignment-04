# --------------PROGRAM STATEMENT
'''
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
'''

# constant value
inches: int = 12

def main():
# input from user of feet's
    feet: float = float(input("Enter the number of feet to change it into inches: "))
# concatenation to convert int and float into str
    print("Feet = " + str(feet) + " ft")
    print("Constant Inches = " + str(inches) + " inch")
# formula
    measure = feet * inches
    print(f"Feet is equals to {measure} inches")

# calling function
if __name__ == "__main__":
    main()