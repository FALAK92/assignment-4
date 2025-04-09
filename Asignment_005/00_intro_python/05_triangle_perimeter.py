def calculate_perimeter():
    
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))


    perimeter = side1 + side2 + side3

    
    print(f"The perimeter of the triangle is: {perimeter}")


if __name__ == "__main__":
    calculate_perimeter()
