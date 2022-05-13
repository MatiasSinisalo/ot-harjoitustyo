
import json
#help for saving to json: https://docs.python.org/3/library/json.html 
#help for opening files: https://docs.python.org/3/library/functions.html#open 
class FileSaver:
    """Class for saving a single dictionary of data to a file. Which is currently test.json"""
    def __init__(self) -> None:
        """Inits the data dictionary and file variable"""
        self.data = {}
        self.open_file = None
        pass
   
    def save_dict_to_file(self, file):
        """Saves the data dictionary to a file and closes the file

            Args:
                    file: filehandle to file

        """
        json.dump(self.data, file)
        file.close()
    
    def bind_data_to_save(self, primary_key, data):
        """Puts data inside the data dictionary with a key of primary_key
              
            
        
        """
        self.data[primary_key] = data

    def read_dict_from_file(self, file):
        """Reads a single dictionary from a file and closes the file

            Args:
                    file: filehandle to file
        
        
            Returns:
                Dictionary containing the app state with keys 
                        cell_values: contains the cell values
                    
                        chart_values: contains a dictionary of chart information
        """
        try:
            data = json.load(file)
            file.close()
            return data

        except:
            return None
       
       
     
        
        
        



