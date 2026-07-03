# Expense Tracker

FILE_NAME = "expenses.txt"


def add_expense():
    """Add a new expense to the file."""
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        category = input("Enter category (Food, Travel, Shopping, etc.): ").strip()
        description = input("Enter description: ").strip()

        with open(FILE_NAME, "a") as file:
            file.write(f"{amount},{category},{description}\n")

        print("Expense added successfully!")

    except ValueError as e:
        print("Invalid input:", e)


def view_expenses():
    """Display all expenses."""
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

            if not expenses:
                print("No expenses recorded.")
                return

            print("\n--- Expense Records ---")
            for expense in expenses:
                amount, category, description = expense.strip().split(",")
                print(
                    f"Amount: ₹{amount} | Category: {category} | Description: {description}"
                )

    except FileNotFoundError:
        print("No expense file found.")


def summarize_expenses():
    """Calculate total expense by category."""
    category_totals = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                amount, category, description = line.strip().split(",")

                amount = float(amount)

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

        if not category_totals:
            print("No expenses to summarize.")
            return

        print("\n--- Expense Summary ---")
        grand_total = 0

        for category, total in category_totals.items():
            print(f"{category}: ₹{total:.2f}")
            grand_total += total

        print(f"\nTotal Expenses: ₹{grand_total:.2f}")

    except FileNotFoundError:
        print("No expense file found.")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_expense()

            elif choice == 2:
                view_expenses()

            elif choice == 3:
                summarize_expenses()

            elif choice == 4:
                print("Goodbye!")
                break

            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid choice! Please enter a number.")


main()