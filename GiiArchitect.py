import csv
import os

filePath = str(input())
os.chdir(filePath)
print(str(os.getcwd))

print("It worked " + str(os.getcwd()))

fileName = str(input())
with open(fileName, newline="") as f:
    spamreader = csv.reader(f)
    for row in spamreader:
        os.mkdir(row[0])
        continue
            
            
