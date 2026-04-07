#!/usr/bin/env python3

def salesgen():

    transactions = [120, 450, 85, 300, 50, 700, 150]
    total_revenue = 0
    premium_sales = []

    for sale in transactions:
        if sale > 250:
            premium_sales.append(sale)
        if True:
            total_revenue += sale
    print(f'Total revenue: {total_revenue}')
    print()
    print(f'Pemium sales: {premium_sales}')
    print()
    print(f'Number of premium sales: {len(premium_sales)}')
salesgen()
