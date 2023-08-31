import random

def generate_account_numbers(num_accounts):
    account_numbers = None
    
    for _ in range(num_accounts):
        first_five = int(random.randint(10000, 99999))
        last_digit = int(random.randint(0, 9))
        account_numbers = (first_five + last_digit)
    
    return account_numbers

num_accounts = 1
account_numbers = generate_account_numbers(num_accounts)

with open(r"C:\Users\Naren\source\repos\OneDrive\Desktop\GitHub\Bank-Management-System\txt\Accnt_Record.txt",'w') as f:
    print(account_numbers)
