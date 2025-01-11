from transliterate import translit
import os
from dotenv import load_dotenv

load_dotenv()

class JSONformatter:
    fileName = ""
    generalName = os.getenv("CONFIG_TITLE")
    jsonObject = ""
    inputLines = []
    partsTitles = {}
    partsTexts = {}
    textConfig = {}

    def __init__(self, fileName, inputLines) -> None:
        self.fileName = fileName.split(".")[0]
        self.inputLines = inputLines
        self.partsTitlesFormatter()
        self.partsTextFormatter()

    def handle(self):
        return {
            'filename': self.fileName,
            'partsTitles': self.partsTitles,
            'partsTexts': self.partsTexts,
            'textConfig': self.textConfig,
        }

    def partsTitlesFormatter(self):
        for part in self.inputLines:
            title = self.titleClearing(part[0])
            self.partsTitles[title] = part[0].replace(
                "\n", "").replace("﻿", "")
            self.partsTexts[title] = part[1:]

    def titleClearing(self, title):
        preTranslit = title.split(" ")[1].lower()
        return self.clearString(translit(preTranslit, reversed=True))

    def partsTextFormatter(self):
        for key, part in self.partsTexts.items():
            self.partsTexts[key] = self.partToObject(part,key)
            self.textConfig[key] = list(self.partsTexts[key].keys())

    def partToObject(self, part,topTitle):
        """ transform array of lines to object transliterated_heading: original_line """
        partObject = {}
        currentHeading = ""
        for line in part:
            if line[0].isdigit():
                currentHeading = self.generalName +"."+topTitle + "." + "_".join(
                    map(self.textPartClearing, line.split(" ")[1:6]))
                print("Heading: " + currentHeading)
                partObject[currentHeading] = self.textLineClearer(line) 
            else:
                partObject[currentHeading] += "\n" + line.replace("* ","• ")
        return partObject

    def textPartClearing(self, line):
        """ create transliterated heading from line start """
        newline = self.clearString(line).lower()
        translatedLine = ""
        try:
            translatedLine = translit(newline, reversed=True) if newline != "" else ""
        except:
            print(newline) 
        
        return self.clearString(translatedLine)

    def clearString(self,line):
        """ remove unneeded characters for title """
        wrongCharachters = [',','.',"'",")","(","\n",'-','є','ї',"__","’",":","/"]
        for item in wrongCharachters:
            line = line.replace(item,"")
        unambiguosLine = line.replace("і","i")
        return unambiguosLine
    
    def textLineClearer(self,line):
        """ 
        remove last \n 
        remove first numbers like 1.1
        transform * to 

        """
        lineWithDiscs = line.replace("* ","• ")
        lineWithoutEnding = lineWithDiscs[0:len(lineWithDiscs)-1]
        
        return lineWithoutEnding[lineWithoutEnding.find(" ")+1:]