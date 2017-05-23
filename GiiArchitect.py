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
        pathBank = filePath
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
                    line = line.replace(char, "")
                titles.append(line)
                continue
                
        #for each title in list titles, make a directory in cwd
        #create a file "archi.txt" inside each new directory
        for title in titles:
            os.mkdir(title.rstrip('\n'))
            newDir = pathBank + "/" + title.rstrip('\n')
            os.chdir(newDir)
            newText = open("archi.txt","w+")
            #print(os.getcwd())
            os.chdir(pathBank)
            print(os.getcwd())
            print(title.rstrip('\n') + " created in " + os.getcwd()) 
            continue
               
    except (KeyboardInterrupt, SystemExit):
        continue
    except (FileNotFoundError, OSError, FileExistsError):
        print ("Error: There was an issue.\nMake sure your filepath is correct and that you are not trying to create directories that already exist.\nStarting over.\n")
        continue
