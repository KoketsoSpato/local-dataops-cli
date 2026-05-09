from validate import Validator
from transform import Transformer
from storage import Storage
import json
from utils import Tools
import time
from logger_config import logger

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
                        logger.error(f"study.csv | Row {index} | {problems}") # log change
                    else:
                        clean_data.append(tranformer.transform_study(index,line))
                storage.save(clean_data,"store/study.json")
                # print(data)
        except FileNotFoundError as e:
            logger.error(f"FileNotFound : {e}")
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
                        logger.error(f"expenses.json | Row {index} | {problems}")
                    else:
                        clean_data.append(tranformer.transform_expense(index,obj))
                storage.save(clean_data,store_expense_path)
        except FileNotFoundError as e:
            logger.error(f"FileNotFound : {e}")
        end = time.time()
        return tool.get_time(end,start)        
        

