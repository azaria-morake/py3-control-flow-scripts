#!/usr/bin/env python3

user_role = input("Enter user role: ")
authentication = input("Enter bool: ")

if authentication == "True":
    is_authenticated = True
else:
    is_authenticated = False

def access(user_role, is_authenticated):
    if is_authenticated == False:
        print("Access Denied: Please log in.")
    elif is_authenticated == True and user_role == "admin":
        print("Welcome, Overlord. Vault access granted.")
    elif is_authenticated == True and user_role == "guest":
        print("Limited access granted. You may view the lobby.")
    else:
        print("Access Denied: Invalid Role.")

access(user_role, is_authenticated)
