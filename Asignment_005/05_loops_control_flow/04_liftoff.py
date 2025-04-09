#Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!
#Here's a sample run of the program:
#10 9 8 7 6 5 4 3 2 1 Liftoff!

import time  # Countdown delay ke liye
from rich.console import Console  # CLI colors aur effects ke liye

# Rich console object
console = Console()

def spaceship_launch():
    console.print("[bold cyan]🚀 Preparing for launch...[/bold cyan]\n")
    
    # Countdown loop
    for i in range(10, 0, -1):
        console.print(f"[bold yellow]{i}...[/bold yellow] ⏳", end=" ", style="bold")
        time.sleep(1)  # 1 second delay for real countdown effect

    # Liftoff message with animation
    console.print("\n[bold green]🔥 3...[/bold green]", style="bold")
    time.sleep(1)
    console.print("[bold blue]🚀 2...[/bold blue]", style="bold")
    time.sleep(1)
    console.print("[bold red]🌍 1...[/bold red]", style="bold")
    time.sleep(1)

    console.print("[bold magenta]🚀🔥 Liftoff! We have a liftoff! 🌍✨[/bold magenta]")

# Function call
spaceship_launch()
