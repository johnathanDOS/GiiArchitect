import csv
import os

while True:
    try:
        #request a filepath from the user
        print("START: Input filepath where new directories should be created.")
        filePath = str(input())
        os.chdir(filePath)
        filePath = "clear"
        print("Current working directory: " + str(os.getcwd()) + "\n")

        #request a .txt file from the user
        print("Input filepath of .txt file new directories should be extracted from.")
        fileName = str(input())
        fileName = fileName.replace('"', '')
        
      
        with open(fileName, "rt") as f:
            for linenum, line in enumerate(f):
                os.mkdir(line.rstrip('\n'))
                print(line.rstrip('\n') + " created in " + os.getcwd()) 
                continue
                
    except (KeyboardInterrupt, SystemExit):
        continue
    except (FileExistsError):
        print("Error: Cannot create a directory when that directory already exists. Make sure you are working in an empty directory, then try again\n")
        continue
            
            
