# --------------PROGRAM STATEMENT
'''
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula e = mc^2
'''


# exp-1
# constant value of speed
c = 299792458

# using while for continually reading mass from user
while True:
# try for correct input
    try:
        mass = float(input("Enter the value of mass in kg: "))
# making data
        print("---Data---")
        print(f"c = {c} m/s")
        print(f"mass = {mass} kg")
# formula and solution
        energy = mass * c ** 2
        print("Formula:-- e = mc^2 ")
        print(f"e = {energy} joules")
# using except for incorrect input
    except:
        print("Please enter a valid number for the mass")
# input field for continuing loop
    mass_continue = input("Do you want to enter another mass? (yes/no): ")
# if not then break
    if mass_continue != "yes":
        break


print("=" * 80)


# exp-2
c: int = 299792458

def main():
    mass: float = float(input("Enter the value of mass in kg: "))
# making data
    print("---Data---")
    print("c = " + str(c) + " m/s")
    print("m = " + str(mass) + " kg")
# formula and solution
    energy = mass * c ** 2
    print("---Formula---")
    print("e = mc^2")
    print("e = " + str(energy) + " joules")

# calling function
if __name__ == "__main__":
    main()