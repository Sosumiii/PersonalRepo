from bankaccount import BankAccount

def main():
    start_val = 100
    savings = BankAccount(start_val)
    print(savings.getBalance())
    savings.deposit(1000)
    print(savings.getBalance())
    savings.withdraw(400)
    print(savings.getBalance())
    print(savings)

if __name__ == "__main__":
    main()