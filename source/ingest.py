from validate import Validator
from transform import Transformer
from storage import Storage
import json
from utils import Tools
import time
class IngestService:

    
    def read_study(self):
        tool = Tools()
        start = time.time()
        try:
            with open("input/study.csv","r") as file:
                headings = file.readline()
                contents = file.readlines()
                clean_data = []
                error = Validator()
                storage = Storage()
                tranformer = Transformer()
                for index,line in enumerate(contents):
                    index+=1
                    problems = error.validate_study(line)
                    if problems:
                        storage.write_logs(index,problems,"input/study.csv")
                    else:
                        clean_data.append(tranformer.transform_study(index,line))
                storage.save(clean_data,"store/study.json")
                # print(data)
        except FileNotFoundError as e:
            print(f"FileNotFoundError : {e}")
        end = time.time()
        return tool.get_time(end,start)
    
        

    def read_expense(self):
        tool = Tools()
        start = time.time()
        try:
            with open("input/expenses.json","r") as file:
                data = json.load(file)
                clean_data = []
                error = Validator()
                storage = Storage()
                tranformer = Transformer()
                input_expense_path = "input/expenses.json"
                store_expense_path = "store/expenses.json"
                for index,obj in enumerate(data):
                    index+=1
                    problems = error.validate_expense(obj) 
                    if problems:
                        storage.write_logs(index,problems,input_expense_path)
                    else:
                        clean_data.append(tranformer.transform_expense(index,obj))
                storage.save(clean_data,store_expense_path)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
        end = time.time()
        return tool.get_time(end,start)        
        

