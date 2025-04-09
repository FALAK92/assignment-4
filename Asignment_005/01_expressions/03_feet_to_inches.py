#Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.


INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  #user se input lenge
    inches: float = feet * INCHES_IN_FOOT  # formula
    print("That is", inches, "inches!")
    
    

if __name__ == '__main__':
    main()

