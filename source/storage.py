from datetime import datetime,date
import json
class Storage:

    def save(self,clean_data,source_path):
        try:
            with open(source_path, 'w') as file:
                json.dump(clean_data, file, indent=4)
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")

    def write_logs(self,index,error,path):  
        try:
            with open("output/errors.log","a") as file:
                sentence= f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {path.split("/")[1].split(".")[0].upper()} | {path}:{index} | {error}"
                file.write(sentence+'\n')
        except FileNotFoundError as e:
            print(f"FileNotFoundError : {e}")

    def load(self,path):
        try:
            with open(path,'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError as e:
            print(f"FileNotFoundError: {e}")
