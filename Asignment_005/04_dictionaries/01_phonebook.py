#In this program we show an example of using dictionaries to keep track of information in a phonebook.

# ANSI escape code for blue text
BLUE = "\033[34m"
RESET = "\033[0m"

def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        print(f"{BLUE}{name}{RESET}")  # Print input in blue
        if name == "":
            break
        number = input("Number: ")
        print(f"{BLUE}{number}{RESET}")  # Print input in blue
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")

def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        print(f"{BLUE}{name}{RESET}")  # Print input in blue
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

# Python boilerplate.
if __name__ == '__main__':
    main()
