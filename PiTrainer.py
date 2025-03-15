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
from collections import deque

pi_digits_json = requests.get('https://api.pi.delivery/v1/pi?start=0&numberOfDigits=100&radix=10').json()
pi_digits = pi_digits_json['content']

digit_input = deque()   # Stores user input to print

while True:
    print("Input Digit: ", end="", flush=True)
    key = msvcrt.getch()  # Captures a single key press
    if key.decode() == 'e': 
        break
    
    # User Input is stored to first 30 digits 
    digit_input.append(key.decode())    
    if len(digit_input) > 30:
        digit_input.popleft()
    print("".join(digit_input))
    # print("\nYou pressed:", key.decode())  # Decode to convert bytes to string
