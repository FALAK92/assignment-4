#PROBLEM # 2:
#index_game

def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]
    else:
        return "Index out of range."

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return "Element updated."
    else:
        return "Index out of range."

def slice_list(my_list, start, end):
    if 0 <= start <= end <= len(my_list):
        return my_list[start:end]
    else:
        return "Invalid slice range."

def main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Welcome to the Index Game!")
    print("Your list is:", my_list)

    while True:
        print("\nChoose an operation: access, modify, slice, or quit")
        choice = input("Your choice: ").lower()

        if choice == 'access':
            index = int(input("Enter index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == 'modify':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print(result)
            print("Updated list:", my_list)

        elif choice == 'slice':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == 'quit':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

main()
