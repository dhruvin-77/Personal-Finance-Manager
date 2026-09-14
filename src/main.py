from file_manager import load_transactions, save_transactions
from transaction_manager import TransactionManager
from report_manager import ReportManager

def main_menu():
    print("\n==== Personal Finance Manager ====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Delete Transaction")
    print("5. Show Summary Report")
    print("6. Show Monthly Report")
    print("7. Save & Exit")

def main():
    transactions = load_transactions()
    tm = TransactionManager(transactions)
    print("Loaded", len(transactions), "transactions.")

    while True:
        main_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            tm.add_income_interactive()

        elif choice == "2":
            tm.add_expense_interactive()

        elif choice == "3":
            tm.view_transactions()

        elif choice == "4":
            try:
                tid = int(input("Enter transaction id to delete: ").strip())
            except ValueError:
                print("Invalid id.")
                continue
            ok = tm.delete_transaction(tid)
            print("Deleted." if ok else "Transaction not found.")

        elif choice == "5":
            ReportManager.pretty_print_summary(tm.get_all())

        elif choice == "6":
            try:
                year = int(input("Enter year (YYYY): ").strip())
                month = int(input("Enter month (1-12): ").strip())
                if not (1 <= month <= 12):
                    raise ValueError
            except ValueError:
                print("Invalid year/month.")
                continue
            month_tx = tm.transactions_by_month(month, year)
            print(f"\nTransactions for {year}-{month:02d}:")
            if not month_tx:
                print("No transactions found for this month.")
            else:
                for t in month_tx:
                    print(f"{t.id}. {t.date} | {t.type} | ₹{t.amount:.2f} | {t.category} | {t.note}")
            print()
            ReportManager.pretty_print_summary(month_tx)

        elif choice == "7":
            save_transactions(tm.get_all())
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
