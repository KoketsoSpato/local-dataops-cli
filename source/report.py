from storage import Storage

class ReportService:

    def study_report(self):
        storage = Storage()
        data = storage.load("store/study.json")

        if not data:
            print("No study data found.")
            return

        total_minutes = sum(item["minutes"] for item in data)
        avg_minutes = total_minutes / len(data)

        print("\n=== Study Report ===")
        print(f"{'Total Sessions':<18} : {len(data)}min\n"
              f"{'Total Minutes':<18} : {total_minutes}min\n"
              f"{'Average':<18} : {avg_minutes:.2f}min\n")

    def expense_report(self):
        
        storage = Storage()
        data = storage.load("store/expenses.json")
        
        # leave the function if there is no data found
        if not data:
            print("No expense data found.")
            return

        total_amount = sum(float(item["amount"]) for item in data)

        category_totals = {}
        for item in data:
            cat = item["category"]
            category_totals[cat] = category_totals.get(cat, 0) + float(item["amount"])

        print("\n=== Expense Report ===")
        print(f"{'Total Expenses':<18} : R{total_amount:.2f}")

        print("\nBy Category:")
        for cat, amount in category_totals.items():
            print(f"{cat:<18} : R{amount:.2f}")