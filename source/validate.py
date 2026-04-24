from datetime import datetime,date
import re

class Validator:
    
    def validate_study(self,line):
        try:
            clean_line = line.strip().split(",")
            # Check if the csv line is not empty
            if clean_line==[""]:
                raise Exception("line is empty")
                
            dates,topic,minutes = clean_line
            # Valid date
            valid_date = datetime.strptime(dates,"%Y-%m-%d")
            # Non empty Topic
            if not topic.strip():
                raise Exception("GeneralError: the topic is empty")
            # Minutes are integer and greater than 0
            valid_minutes = int(minutes)
            if valid_minutes < 0:
                raise ValueError(f"minutes must be a positive integer: {valid_minutes}")
        except ValueError as e:
            return f"ValueError: {e}"
        except Exception as e:
            return f"GeneraError: {e}"
        return None
    
    
    def validate_expense(self,obj):
        try:
            

            if len(obj)!=4:
                raise Exception("GeneralError: incomplete expense record")
            
            date,category,amount,note = [obj[key] for key in obj]
            # Valid date
            valid_date = datetime.strptime(date,"%Y-%m-%d")
            #Non Empty category
            if not category:
                raise Exception("GeneralError: missing category value")
            # Amount is a real Number and greater than 0 : 5
            if not isinstance(amount,(int|float)):
                raise ValueError(f"amount is not a real number : {amount}")
            
            if amount < 0:
                raise ValueError(f"amount is not a postive real number : {amount}")
            # note must be a str
            if not isinstance(note,str):
                raise ValueError("note is not a string")
        except KeyError as e:
            return f"Missing Key: {e}"
        except ValueError as e:
            return f"ValueError: {e}"
        except Exception as e:
            return f"{e}"
        return None
