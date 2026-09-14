from typing import List, Dict
from transaction_manager import Transaction

class ReportManager:
    @staticmethod
    def summary(transactions: List[Transaction]) -> Dict[str, float]:
        income = sum(t.amount for t in transactions if t.type == "income")
        expense = sum(t.amount for t in transactions if t.type == "expense")
        balance = income - expense
        return {"income": income, "expense": expense, "balance": balance}

    @staticmethod
    def category_breakdown(transactions: List[Transaction]) -> Dict[str, float]:
        breakdown = {}
        for t in transactions:
            if t.type != "expense":
                continue
            key = t.category or "Uncategorized"
            breakdown[key] = breakdown.get(key, 0.0) + t.amount
        return breakdown

    @staticmethod
    def pretty_print_summary(transactions: List[Transaction]):
        if not transactions:
            print("No data to generate report.")
            return
        s = ReportManager.summary(transactions)
        print("\n--- Summary Report ---")
        print(f"Total Income  : ₹{s['income']:.2f}")
        print(f"Total Expense : ₹{s['expense']:.2f}")
        print(f"Balance       : ₹{s['balance']:.2f}\n")

        breakdown = ReportManager.category_breakdown(transactions)
        if breakdown:
            print("Category-wise Expense:")
            for cat, amt in sorted(breakdown.items(), key=lambda x: -x[1]):
                print(f"{cat} : ₹{amt:.2f}")
        else:
            print("No expense categories recorded.")
        print()
