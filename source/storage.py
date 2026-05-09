from datetime import datetime,date
from logger_config import logger
import json
class Storage:

    def save(self,clean_data,source_path):
        try:
            with open(source_path, 'w') as file:
                json.dump(clean_data, file, indent=4)
        except FileNotFoundError as e:
            logger.error(f"FileNotFound : {e}")


    def load(self,path):
        try:
            with open(path,'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError as e:
            logger.error(f"FileNotFound : {e}")
