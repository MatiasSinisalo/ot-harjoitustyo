import csv
#help for saving to csv: https://docs.python.org/3/library/csv.html
class FileSaver:
    def __init__(self) -> None:
        pass
   
    def SaveDictToFile(self, path, data):
        try:
            file = open("test.csv", "w")
            writer = csv.DictWriter(file, fieldnames=data.keys())
            writer.writeheader()
            writer.writerow(data)
            file.close()
        except:
            print("virhe tiedostoa luodessa!")
            
            
           
        
        
    
    def readDictFromFile(self, path):
        try:
            with open("test.csv", "r") as file:
                returnData = []
                reader = csv.DictReader(file, delimiter=",")
                for val in reader:
                    returnData.append(val)
                file.close()
                return returnData
        except:
            print("testi.csv tiedostoa ei olemassa")
       
       
     
        
        
        



