#!/usr/bin/env python3

numbers = [1,2,5,3,4]

number = int(input("Enter number to find: "))

def findloc(numbers, number):

    count = 0
    for num in numbers:
        if num == number:
             location = print(count)
        count+=1
    return location

findloc(numbers, number)
