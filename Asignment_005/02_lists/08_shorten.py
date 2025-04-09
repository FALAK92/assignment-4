#Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, 
# and prints each item it removes until lst is MAX_LENGTH items long. 
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your 
# function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Jab tak list ka size MAX_LENGTH se bada hai
        last_elem = lst.pop()  # List ka last element remove karo
        print(last_elem)  # Remove hone wala element print karo

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []  # Empty list banai
    elem = input("Please enter an element of the list or press enter to stop. ")  # Pehla input lo
    while elem != "":  # Jab tak user empty input na de
        lst.append(elem)  # List me element add karo
        elem = input("Please enter an element of the list or press enter to stop. ")  # Next input lo
    return lst  # Puri list return karo


def main():
    lst = get_lst()  # User se list input lo
    shorten(lst)  # List ko `shorten()` function me pass karo

if __name__ == '__main__':
    main()
