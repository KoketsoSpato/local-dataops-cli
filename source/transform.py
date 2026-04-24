from datetime import datetime,date
from unicodedata import category


class Transformer:
    """Data will be clean then """
    def transform_study(self,index : int ,study_record : str) -> dict:
        """Clean the study data after they are validated"""
        clean_record = study_record.strip().split(',')
        dates,topic,minutes = clean_record
        valid_date = datetime.strptime(dates,"%Y-%m-%d")
        input_Study_path = "input/study.csv"
        return {
            "id": index,
            "date": f"{valid_date.date()}",
            "topic": topic.strip().upper(),
            "minutes": int(minutes),
            "created_at": f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}",
            "source_file": input_Study_path
        }



    # clean the expenses
    def transform_expense(self,index : int,expense_record : dict) -> dict:
        """Clean the expenses data after then are validated"""
        date,category,amount,note = [expense_record[key] for key in expense_record]
        valid_date = datetime.strptime(date,"%Y-%m-%d")
        input_expense_path = "input/expenses.json"
        return {
            "id": index,
            "date": f"{valid_date.date()}",
            "category": category.title(),
            "amount": f"{amount:.2f}",
            "note": note.title(),
            "created_at": f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}",
            "source_file": input_expense_path
        }


