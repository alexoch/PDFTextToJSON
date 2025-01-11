from services import FileIO
from services import JSONformatter

def transform():
    fileHandler = FileIO.FileIO()
    inputLines = fileHandler.input()
    fileName = fileHandler.input_file
    jsonFormatter = JSONformatter.JSONformatter(fileName,inputLines)
    fileHandler.output(jsonFormatter.handle())


if __name__ == "__main__":
    transform()
        