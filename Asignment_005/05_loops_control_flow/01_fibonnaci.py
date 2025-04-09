#Write a program that displays the terms in the Fibonacci sequence, 
# starting with Fib(0) and continuing as long as the terms are less than 10,000 (you should store this value as a constant!).
# Thus, your program should produce the following sample run:
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
MAX_TERM_VALUE: int = 10000  # Fibonacci series will go up to 10,000 🚀

# ANSI color codes
YELLOW = "\033[93m"
PURPLE = "\033[95m"  
ORANGE = "\033[91m"  
RESET = "\033[0m"  

def main():
    print(f"{YELLOW}🎯 Let's Generate Fibonacci Numbers Up to 10000!{RESET}\n")  # Yellow heading
    
    curr_term = 0  # First number is 0
    next_term = 1  # Second number is 1
    step = 1  # To keep track of steps

    while curr_term <= MAX_TERM_VALUE:
        print(f"🔹 Step {step}: {ORANGE}{curr_term}{RESET}")  # Answer in gray
        step += 1  # Move to the next step
        
        # Calculate the next number
        term_after_next = curr_term + next_term
        print(f"    ➡️ {PURPLE}{curr_term} + {next_term} = {term_after_next}{RESET} (Next Term)\n")  # Calculation in purple
        
        # Update values for the next loop
        curr_term = next_term
        next_term = term_after_next

# This part runs the main function (boilerplate code)
if __name__ == '__main__':
    main()



