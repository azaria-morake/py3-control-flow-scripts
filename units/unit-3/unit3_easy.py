#!/usr/bin/env python3

def posfilt():
    numbers = [10, -5, 3, -1, 7, 22, -15, 0]
    positive_numbers = []

    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
        else:
            pass

    print(positive_numbers)

posfilt()
