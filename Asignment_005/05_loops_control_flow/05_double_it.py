#Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.
#For example if the user enters the number 2 you would then print:
#4 8 16 32 64 128

def double_until_100():
    num = int(input("Enter a number: "))  # Get user input
    while num < 100:  # Repeat until number reaches or exceeds 100
        num *= 2  # Double the number
        print(num, end=" ")  # Print the doubled number on the same line

double_until_100()
