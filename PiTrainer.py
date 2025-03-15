# Features
"""
- Mistakes are fine lol, it just won't let you move on for a bit (if wrong digit, print "wrong")
- Type "e" to end, or ends when reached # digits to recite
- Set how many digits you want to recite
- Infinite mode tbd
- If you want to start from the middle, we preview previous 10 digits
- Check if it is a digit, only submit if it is a digit or EOF
- TKinter UI with cute girls TBD as well
- NOTE: No need for user to add . but they do need to start with 3
- Print the digits on the bottom as user progresses? (scroll with 30 digits?)
"""

import msvcrt
import requests
import os
from collections import deque

def get_pi_digits(start):
    pi_digits_json = requests.get(f'https://api.pi.delivery/v1/pi?start={start}&numberOfDigits=100&radix=10').json()
    pi_digits = pi_digits_json['content']
    return deque(pi_digits)


def main():
    digit_input = deque()   # Stores user input to print

    start = 0 # Digit number that pi recitation starts at

    print("How many digits would you like to recite (type infinite for neverending): ")
    digit_limit = input()
    digit_count = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    pi_digits = get_pi_digits(start)

    next_digit = pi_digits.popleft()

    while True if digit_limit == "infinite" else digit_count < int(digit_limit):
        print("Input Digit: ", flush=True)
        key = msvcrt.getch()  # Captures a single key press
        if key.decode() == 'e': 
            break
        
        # Invalid Input check
        if not key.decode().isnumeric():
            print("Invalid Input. Please input a digit (0-9)")
            continue
        
        # Is it correct digit?
        if key.decode() != next_digit:
            print("Wrong! Try again.")
            continue

        # Get next digit
        next_digit = pi_digits.popleft()

        digit_count += 1    # update digit count

        # User Input is stored to first 30 digits 
        digit_input.append(key.decode())    
        if len(digit_input) > 30:
            digit_input.popleft()

        os.system('cls' if os.name == 'nt' else 'clear')
        print("".join(digit_input))

        if len(pi_digits) == 0:
            start += 100
            pi_digits = get_pi_digits(start)
        

if __name__ == "__main__":
    main()