balance = 0
while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Amount deposited: {amount}")
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"Amount withdrawn: {amount}")
    elif choice == 3:
        print(f"Current balance: {balance}")
    elif choice == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")