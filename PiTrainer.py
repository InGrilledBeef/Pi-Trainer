# Features
"""
- Mistakes are fine lol, it just won't let you move on for a bit (if wrong digit, print "wrong")
- ype "e" to end
- Set how many digits you want to recite
- Infinite mode tbd
- If you want to start from the middle, we preview previous 10 digits
- Check if it is a digit, only submit if it is a digit or EOF
- TKinter UI with cute girls TBD as well
"""

import msvcrt


while True:
    print("Press any key: ", end="", flush=True)
    key = msvcrt.getch()  # Captures a single key press
    if key.decode() == 'e': 
        break
    
    print("\nYou pressed:", key.decode())  # Decode to convert bytes to string
    # char = sys.stdin.read(1)  # Read one character at a time
    # if not char:  # EOF reached
    #     break
    # print(f"Read char: {char}", end="")
