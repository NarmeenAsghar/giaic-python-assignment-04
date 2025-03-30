#-------PROGRAM STATEMENT:
'''
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
'''

# exp-1
# creating function
def main():
    animal = input("What's your favourite animal? ") # input with question
    print("My favourite animal is also", animal, ".") # output

if __name__ == "__main__":
    main()  # calling function


print("=" * 100)

# exp-2
# simple python code
question = "What's your favourite animal?"
print(question)

answer = input("Enter your answer: ")
print("My favuorite animal is", answer)