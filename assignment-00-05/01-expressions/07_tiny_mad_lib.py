# --------------PROGRAM STATEMENT
'''
Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
'''

def main():
# input from user for an adjective, noun, and verb to create a Python development story
    adjective = input("Please type an adjective to describe programming: ")
    noun = input("Please type a noun related to coding: ")
    verb = input("Please type a verb related to programming: ")

# story using the inputs
    story = f"Once upon a time, there was a {adjective} developer who loved to code in Python. Every day, they worked on a {noun} project and would {verb} until the code ran perfectly. They became a Python expert and made amazing programs!"

# output
    print(story)

# calling function
if __name__ == "__main__":
    main()
