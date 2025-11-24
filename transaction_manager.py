from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Transaction:
    id: int
    date: str         
    type: str 
    amount: float   
    category: str
    note: str = ""

class TransactionManager:
    def __init__(self, transactions: Optional[List[Transaction]] = None):
        self.transactions: List[Transaction] = transactions or []

    def _next_id(self) -> int:
        if not self.transactions:
            return 1
        return max(t.id for t in self.transactions) + 1

    def create_transaction(self, t_type: str, amount: float, category: str = "", note: str = "") -> Transaction:
        t = Transaction(
            id=self._next_id(),
            date=datetime.now().strftime("%Y-%m-%d"),
            type=t_type,
            amount=float(amount),
            category=category,
            note=note
        )
        self.transactions.append(t)
        return t

    def add_income_interactive(self):
        try:
            amount = float(input("Enter income amount: ").strip())
        except ValueError:
            print("Invalid amount. Cancelled.")
            return

        source = input("Enter income source/category (optional): ").strip()
        t = self.create_transaction("income", amount, category=source)
        print(f"Income added (id={t.id}).")

    def add_expense_interactive(self):
        try:
            amount = float(input("Enter expense amount: ").strip())
        except ValueError:
            print("Invalid amount. Cancelled.")
            return

        category = input("Enter expense category (e.g., food, travel): ").strip()
        note = input("Enter note (optional): ").strip()
        t = self.create_transaction("expense", amount, category=category, note=note)
        print(f"Expense added (id={t.id}).")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions recorded yet.")
            return
        print("\n--- Transactions ---")
        for t in sorted(self.transactions, key=lambda x: x.id):
            print(f"{t.id}. {t.date} | {t.type.capitalize():7} | ₹{t.amount:.2f} | {t.category or '-'} | {t.note or '-'}")
        print()

    def delete_transaction(self, tid: int) -> bool:
        for i, t in enumerate(self.transactions):
            if t.id == tid:
                del self.transactions[i]
                return True
        return False

    def get_all(self) -> List[Transaction]:
        return list(self.transactions)

    def transactions_by_month(self, month: int, year: int) -> List[Transaction]:
        result = []
        for t in self.transactions:
            try:
                dt = datetime.strptime(t.date, "%Y-%m-%d")
            except ValueError:
                continue
            if dt.year == year and dt.month == month:
                result.append(t)
        return result
