from utils import Tools
from storage import Storage
from ingest import IngestService
from report import ReportService
from query import QueryService
import json

class CLI:
    #  start running app
    def run(self):
        """Starting running the program"""
        print("=== Local DataOps CLI ===")
        self.menu_selection()
    def menu(self):
        """Displays the main menu and gives user options to choose."""
        print(
            "1) Import data\n"
            "2) Reports\n"
            "3) Query/Filter\n"
            "4) Smart Mode(random)\n" 
            "5) Exit\n"
            )
    def menu_selection(self):
        running = True
        while running:
            self.menu()
            while True:
                try :
                   choice = int(input("Choose:"))
                   break
                except ValueError as e:
                    print(f"ValueError : {e}")
            
            match choice:
                case 1:
                    self.import_datasets()
                case 2:
                    self.get_reports()
                case 3:
                    self.get_queries()
                case 4:
                    print("Smart Mode")
                case 5:
                    running = False
                case _:
                    print("Invalid choice, please try again!!!")


    def import_datasets(self):
        running = True
        while running:
            print("Choose datasets: \n"
              "1. Study (CSV)\n"
              "2. Expenses (JSON)\n"
              )
            
            while True:
                try:
                    choice = int(input("Choose: "))
                    break
                except ValueError as e:
                    print(f"ValueError : {e}")
                
            match choice:
                case 1:
                    self.study_summary()
                    break
                case 2:
                    self.expenses_summary()
                    break
                case _:
                    print("invalid selection, please try again")


    def expenses_summary(self):
        storage = Storage()
        ingest = IngestService()
        #initiate file paths 
        input_expenses_path = "input/expenses.json"
        store_expense_path = "store/expenses.json"
        output_errors_path = "output/errors.log"
       
        try:
            exe_time=ingest.read_expense()
            raw_data=storage.load(input_expenses_path)
            data = storage.load(store_expense_path)
            processed_rows = len(raw_data)
            valid_rows = len(data)
            invalid_rows = processed_rows - valid_rows
            

            print(
            "\nProcessing input/expenses.json ...\n"
            f"{'Rows processed':<18} : {processed_rows}\n"
            f"{'Valid rows':<18} : {valid_rows}\n"
            f"{'Invalid rows':<18} : {invalid_rows}\n"
            f"{'Saved to':<18} : {store_expense_path}\n"
            f"{'Errors logged':<18} : {output_errors_path}\n"
            f"{'Time':<18} : {exe_time:.3f}s \n"
            )
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"GeneralError: {e}")
        
        
    def study_summary(self):
        storage = Storage()
        ingest = IngestService()
        #intiate file paths
        input_study_path = "input/study.csv"
        store_study_path = "store/study.json"
        output_errors_path = "output/errors.log"
    
        try:
            exe_time=ingest.read_study()
            study_file=open(input_study_path,"r")
            raw_study = study_file.readlines()
            study_file.close()
            data = storage.load(store_study_path)
            processed_rows = len(raw_study)-1
            valid_rows = len(data)
            invalid_rows = processed_rows - valid_rows
        
            print(
            f"\nProcessing {input_study_path} ...\n"
            f"{'Rows processed':<18} : {processed_rows}\n"
            f"{'Valid rows':<18} : {valid_rows}\n"
            f"{'Invalid rows':<18} : {invalid_rows}\n"
            f"{'Saved to':<18} : {store_study_path}\n"
            f"{'Errors logged':<18} : {output_errors_path}\n"
            f"{'Time':<18} : {exe_time:.3f}s \n"
            )
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"GeneralError: {e}")
            
        
    
    
    # handle the reports
    def get_reports(self):
    
        report = ReportService()
        running = True
        while running:
            print("Choose Reports: \n"
                  "1) Study Report\n"
                "2) Expense Report\n")

            while True:
                try:
                    choice = int(input("Choose: "))
                    break
                except ValueError as e:
                    print(f"ValueError : {e}")

            match choice:
                case 1:
                    report.study_report()
                    break
                case 2:
                    report.expense_report()
                    break
                case _:
                    print("invalid selection, please try again")
                    break
    
    # handle the queries
    def get_queries(self):
        query = QueryService()
        running = True
        while running:
            print("1) Search Study by Topic\n"
                "2) Filter Expenses by Category\n")

            while True:
                try:
                    choice = int(input("Choose: "))
                    break
                except ValueError as e:
                    print(f"ValueError : {e}")
            match choice:
                case 1:
                    query.search_study_by_topic()
                    break
                case 2:
                    query.filter_expense_by_category()
                    break
                case _:
                    print(f"invalid selection, please try again.")

if __name__ == "__main__":
    app = CLI()
    app.run()
   








