#-------PROGRAM STATEMENT:
'''
Write a program to solve age-related riddle!
'''

# exp-1
# creating function
def main():
    print("The age calculation of all friends!")
    print("=" * 80)

    anthon = 21
    print(f"Anthon is {anthon} years old.")

    beth = 6 + anthon
    print(f"Beth is {beth} years old.")

    chen = 20
    print(f"Chen is {chen} years old.")

    drew = chen + anthon
    print(f"Drew is {drew} years old.")

    ethan = chen
    print(f"Ethan is {ethan} years old.")

# calling function
if __name__ == "__main__":
    main()


print("=" * 80)


# exp-2
# creatting function
def main():
    anthon: int = 21
    beth: int = 6 + anthon
    chen: int = 20 + beth
    drew: int = chen + anthon
    ethan: int = chen

    print("Anthon is " + str(anthon))
    print("Beth is " + str(beth))
    print("Chen is " + str(chen))
    print("Drew is " + str(drew))
    print("Ethan is " + str(ethan))

# calling function
if __name__ == "__main__":
    main()