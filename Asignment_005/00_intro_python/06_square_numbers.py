#Ask the user for a number and print its square (the product of the number times itself).

def square_number():

    print("Enter a number, and I'll compute its square for you:")
    num = float(input("> "))
    square = num * num
    print(f"{num} squared is {square}")


if __name__ == "__main__":
    square_number()


