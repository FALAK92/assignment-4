#Project 6: Countdown Timer

import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        print(time_format, end='\r')  # \r overwrites the line each second
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# Get user input for countdown time in seconds
total_seconds = int(input("Enter the time in seconds for countdown: "))
# Start the countdown
countdown_timer(total_seconds)

