#!/usr/bin/env python3

def banker():
    balance = 1000
    while True:

        choice = int(input("Please enter 1. Balance, 2. Deposit, 3. Withdraw, 4. Exit: "))
        if choice == 1:
            print(balance)
        elif choice == 2:
            deposit = int(input("Enter deposit amount: "))
            balance += deposit
        elif choice == 3:
            withdrawal = int(input("Enter withdrawal amount: "))
            if withdrawal > 0 and withdrawal <= balance:
                balance -= withdrawal
            else:
                print("Insufficient funds.")
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

banker()
