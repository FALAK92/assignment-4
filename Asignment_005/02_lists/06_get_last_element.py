#Fill out the function get_last_element(lst) which takes in a list lst as a parameter 
# and prints the last element in the list. The list is guaranteed to be non-empty, 
# but there are no guarantees on its length.


def get_last_element(lst):
    """
    Prints the last element of a provided list.
    """
    print(lst[-1])  # Last element ko print kar raha hai

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter elements one by one and returns the list.
    """
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # User se list input le raha hai
    get_last_element(lst)  # Last element print karega

if __name__ == '__main__':
    main()


