#Ask the user for two numbers, one at a time, and then print the result of dividing
# the first number by the second and also the remainder of the division.

def main():
    divident: int = int(input("please enter an integer to be divided: "))
    divisor: int = int(input("please enter an integer to divide by: "))
    
    
    quotient: int = divident // divisor
    remainder: int = divident % divisor
    
    print("The result of this division is:" + str(quotient) + " with a remainder of " + str(remainder))
    
    
if __name__ == '__main__':
    main()    