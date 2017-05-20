import csv
import os

illegalChars = ['\\', '/', ':', '*', '?', '"', "<", ">", "|"]
titles = []
titlesCharFix = []

while True:
    try:
        #request a filepath from the user
        print("START: Input filepath where new directories should be created.")
        filePath = str(input())
        os.chdir(filePath)
        filePath = "clear"
        print("Current working directory: " + str(os.getcwd()) + "\n")

        #request a .txt file from the user
        print("Input filepath and file extension of .txt file new directories should be extracted from.")
        fileName = str(input())
        fileName = fileName.replace('"', '')
        
        #read .txt file, iterate over each line, iterate over illegalChars - 
        #if an item in illegalChars exists in a line, replace that item with "~"
        #append each FIXED line to list "titles"
        with open(fileName, "rt") as f:
            for linenum, line in enumerate(f):
                for char in illegalChars:
                    line = line.replace(char, "~")
                titles.append(line)
                continue
                
        #for each title in list titles, make a directory in cwd
        for title in titles:
            os.mkdir(title.rstrip('\n'))
            print(title.rstrip('\n') + " created in " + os.getcwd()) 
            continue
               
    except (KeyboardInterrupt, SystemExit):
        continue
    except (FileExistsError):
        print("Error: Cannot create a directory that already exists.\n\nStarting over.\n\n")
        continue
            
            
