#!/usr/bin/env python3

"""
Password validator with 3 attempts == max
"""

correct_password = "Python123"

def validator():
    for i in range(0, 3):
        usr_pass = input("Enter password: ")
        if usr_pass == correct_password:
            print("Access Granted!")
            break
        elif i < 2:
            print("Incorrect password. Try again.")

        else:
            print("Account Locked. Too many failed attempts.")

validator()
