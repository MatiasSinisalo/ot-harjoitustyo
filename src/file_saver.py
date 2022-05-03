
import json
#help for saving to json: https://docs.python.org/3/library/json.html 
#help for opening files: https://docs.python.org/3/library/functions.html#open 
class FileSaver:
    def __init__(self) -> None:
        self.data = {}
        self.open_file = None
        pass
   
    def save_dict_to_file(self, path):
           file = open("test.json", "w")
           json.dump(self.data, file)
           file.close()
    
    def bind_data_to_save(self, primary_key, data):
        self.data[primary_key] = data
    
   
       
 
    def read_dict_from_file(self, path):
        try:
            file = open("test.json", "r")
            data = json.load(file)
            file.close()
            return data

        except:
            return None
       
       
     
        
        
        



