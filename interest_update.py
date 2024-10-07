"""
Description: Assignment 3
Author: Krish Malhotra
Date: October 6, 2024
"""
import csv
import pprint

balances = {}

insert_file = 'account_balances.txt'
with open(insert_file, 'r') as file:
    for line in file:
        
        account_number, balance = line.strip().split('|')
        
        balances[account_number] = float(balance)
print("Current Balances:")
pprint.pprint(balances)

for account, balance in balances.items():
    if balance < 0:
        rate = 0.10  # 10% for debt
    elif balance < 1000:
        rate = 0.01  # 1% for positive balances less than $1000
    elif balance < 5000:
        rate = 0.025  # 2.5% $1000 and $5000
    else:
        rate = 0.05  # 5% for $5000 or more
    
    #Monthly interest
    balances[account] = balance + ((balance * rate) / 12)

#Display balances after interest 
print("\nBalances After Interest:")
pprint.pprint(balances)

initials = 'KM'  
account_balances = f'updated_balances_{initials}.csv'

with open(account_balances, 'w', newline='') as csvfile:
    csvfile.write('Account,Balance\n')
    for account, balance in balances.items():
        csvfile.write(f'{account},{balance:.6f}\n')  
print(f"\nUpdated balances written to '{account_balances}'")


