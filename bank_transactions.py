"""
Description: Assignment 3
Author: Krish Malhotra
Date: October 6, 2024
"""
import random
import math
import os
from time import sleep

menu_choices = ["D", "W", "Q"]

## Random number between -1000 and 10000
account_balance = float(random.randint(-1000, 10000))

while True:
    # Clears console
    os.system('cls' if os.name == 'nt' else 'clear')

    ## screen width
    screen_width = 40

    ## ATM Display
    print("*" * screen_width)
    print("PIXELL RIVER FINANCIAL".center(screen_width))
    print("ATM Simulator".center(screen_width))
    print(f"Your current balance is: ${account_balance:,.2f}".center(screen_width))
    print("Deposit: D".center(screen_width))
    print("Withdraw: W".center(screen_width))
    print("Quit: Q".center(screen_width))
    print("*" * screen_width)

    # Get user selection
    selection = input("Enter your selection: ").strip().upper()

    if selection not in menu_choices:
        print("*" * screen_width)
        print("INVALID SELECTION".center(screen_width))
        print("*" * screen_width)
        sleep(2)
        continue

    if selection == "Q":
        print("*" * screen_width)
        print(f"Your current balance is: ${account_balance:,.2f}".center(screen_width))
        print("*" * screen_width)
        break

    # Get transaction amount
    amount = float(input("Enter amount of transaction: ".center(screen_width)))

    if selection == "D":
        account_balance += amount
        print("*" * screen_width)
        print(f"Your current balance is: ${account_balance:,.2f}".center(screen_width))
        print("*" * screen_width)

    elif selection == "W":
        if amount > account_balance:
            print("*" * screen_width)
            print("Insufficient Funds".center(screen_width))
            print("*" * screen_width)
        else:
            account_balance -= amount
            print("*" * screen_width)
            print(f"Your current balance is: ${account_balance:,.2f}".center(screen_width))
            print("*" * screen_width)

    # Pause the script for three seconds
    sleep(3)
