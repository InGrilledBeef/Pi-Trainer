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

    start = 1 # Digit number that pi recitation starts at

    print("Would you like to start reciting from the beginning of PI? [yes/no]:", end=" ")
    if input() == 'no':
        print("Where would you like to start? (typing 9 means you want to start at the 9th digit starting from after the decimal point):", end=" ")
        start = int(input())

    print("How many digits would you like to recite (type infinite for neverending): ")
    digit_limit = input()
    digit_count = 0

    os.system('cls' if os.name == 'nt' else 'clear')

    preview = start - 15 if start > 15 else 1   # preview 15 digits before start

    if preview == 1:
        digit_input.appendleft('3.')

    pi_digits = get_pi_digits(preview)

    for i in range(preview, start):
        digit_input.append(pi_digits.popleft())

    next_digit = pi_digits.popleft()

    while True if digit_limit == "infinite" else digit_count < int(digit_limit):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("".join(digit_input))
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
        if len(digit_input) > 50:
            digit_input.popleft()

        if len(pi_digits) == 0:
            start += 100
            pi_digits = get_pi_digits(start)
        
    print("".join(digit_input))  # final output (temp fix)
    print("You recited", digit_count, "number of digits!")

    print("peek ahead:")

    print(''.join(get_pi_digits(start + digit_count)), end="")

if __name__ == "__main__":
    main()