import fileinput
import json
import os
from dotenv import load_dotenv

load_dotenv()

class FileIO:
    input_dir = os.getenv('INPUT_DIR')
    output_dir = os.getenv('OUTPUT_DIR')
    input_file = os.getenv('INPUT_FILE')
    output_file = os.getenv('OUTPUT_FILE')

    def input(self):
        """ 
        read file and create array of arrays with string parts
        
        rtype:[[str]]
        """        
        sequential_enter = 0
        fileLines = []
        partsLines = []
        
        for line in fileinput.input(files=(self.input_dir+self.input_file),encoding="utf-8"):
            if line == "\n":
                sequential_enter += 1
            else:
                partsLines.append(line)
                sequential_enter = 0
            if sequential_enter == 2:
                fileLines.append(partsLines)
                partsLines = []
        
        fileLines.append(partsLines)
        
        return fileLines
    
    def output(self,jsonObject):
        """ 
        writes converted to json object to file in output folder
        returns output file name 
        
        rtype:str
        """
        with open(self.output_dir+self.output_file, 'w', encoding='utf-8') as f:
            json.dump(jsonObject, f, ensure_ascii=False, indent=4)
        return self.output_dir
    