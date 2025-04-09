#Print 10 random numbers in the range 1 to 100.

import random

# Constants
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    This function generates and prints 10 random numbers 
    between 1 and 100.
    """
    # Generate random numbers and store them in a list
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Print the random numbers
    print("Random Numbers:", random_numbers)

# Calling main() when the script runs
if __name__ == '__main__':
    main()


