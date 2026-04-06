#!/usr/bin/env python3

credit_score = int(input("Enter credit score: "))
annual_income = int(input("Enter annual income: "))
boolean = input("Enter True/False for Bankruptcy: ")

if boolean == "True":
    has_bankruptcy = True
else:
    has_bankruptcy = False

def cred_approve(credit_score, annual_income, has_bankruptcy):
    if has_bankruptcy == True:
        print("Application Denied: Prior bankruptcy.")
    elif credit_score > 750 and annual_income > 50000:
        print("Premium Loan Approved.")
    elif credit_score > 600 and annual_income > 30000:
        print("Standard Loan Approved.")
    elif credit_score > 600 or annual_income > 40000:
        print("Manual Review Required.")
    else:
        print("Application Denied: Low score/income.")

cred_approve(credit_score, annual_income, 
   has_bankruptcy)

