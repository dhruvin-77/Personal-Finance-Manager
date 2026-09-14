import csv
from typing import List
from transaction_manager import Transaction

FILENAME = "finance_data.csv"
CSV_HEADER = ["id", "date", "type", "amount", "category", "note"]

def load_transactions(filename: str = FILENAME) -> List[Transaction]:
    transactions = []
    try:
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row or not row.get("id"):
                    continue
                try:
                    t = Transaction(
                        id=int(row["id"]),
                        date=row["date"],
                        type=row["type"],
                        amount=float(row["amount"]),
                        category=row.get("category", "") or "",
                        note=row.get("note", "") or ""
                    )
                except Exception:
                    continue
                transactions.append(t)
    except FileNotFoundError:
        pass
    return transactions

def save_transactions(transactions: List[Transaction], filename: str = FILENAME):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
        writer.writeheader()
        for t in transactions:
            writer.writerow({
                "id": t.id,
                "date": t.date,
                "type": t.type,
                "amount": f"{t.amount:.2f}",
                "category": t.category,
                "note": t.note
            })
