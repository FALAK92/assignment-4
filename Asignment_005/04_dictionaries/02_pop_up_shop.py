#Write a program that loops through a dictionary of fruits, 
# prompting the user to see how many of each fruit they want to buy, 
# and then prints out the total combined cost of all of the fruits.

# ANSI escape codes for pink color
PINK = "\033[95m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
RESET = "\033[0m"

def main():
    fruits = {
        '🍎 apple': 1.5, 
        '🌰 durian': 50, 
        '🍈 jackfruit': 80, 
        '🥝 kiwi': 1, 
        '🍇 rambutan': 1.5, 
        '🥭 mango': 5
    }
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"{BOLD}{ITALIC}How many {PINK}{fruit_name}{RESET}{BOLD}{ITALIC} do you want to buy?: {RESET}"))
        print(f"{PINK}{BOLD}{ITALIC}{amount_bought} {fruit_name}{RESET}")  # Show input in pink
        total_cost += (price * amount_bought)
    
    print(f"{PINK}{BOLD}Your total is ${total_cost}{RESET}")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
