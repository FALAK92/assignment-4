#Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
#For example if the user enters the number 2 you would then print:
#4 8 16 32 64 128


def double_until_100():
    curr_value = int(input("Enter a number: "))  # Get user input
    while curr_value < 100:  # Continue until the value reaches or exceeds 100
        curr_value = curr_value * 2  # Double the value
        print(curr_value, end=" ")  # Print the current value

double_until_100()


