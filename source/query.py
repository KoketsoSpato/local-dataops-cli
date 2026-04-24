from storage import Storage

class QueryService:

    def search_study_by_topic(self):
        storage = Storage()
        data = storage.load("store/study.json")

        keyword = input("Enter topic keyword: ").upper()

        results = [item for item in data if keyword in item["topic"]]

        print(f"\nFound {len(results)} results:\n")
        for record in results:
            print(record)

    def filter_expense_by_category(self):
        storage = Storage()
        data = storage.load("store/expenses.json")

        category = input("Enter category: ").title()

        results = [item for item in data if item["category"] == category]
        print(f"\nFound {len(results)} results:\n")
        for r in results:
            print(r)