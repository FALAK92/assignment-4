# Project 7:
#Password generator

import random
import string

def generate_password(length=12):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for _ in range(length))
    return password

#user input
length = int(input("Enter the desired length of the password: "))

password = generate_password(length)
print(f"Generated password: {password}")
