#Print 10 random numbers in the range 1 to 100.




import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for _ in range(N_NUMBERS):  # Loop for N_NUMBERS times (10 times)
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  # Print random number in the range MIN_VALUE to MAX_VALUE
    print()  # Newline after all numbers

if __name__ == '__main__':
    main()
