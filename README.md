# GiiArchitect Version 1

# Introduction

GiiArchitect is a Python script that iterates over a list of strings in a text file. In our case, these strings will usually be Gemiini script titles. For each string in the list, GiiArchitect creates a new directory in a parent directory specified by the user. Inside each new directory, GiiArchitect places an empty text file called archi.txt so the files can be imported into Adobe Premiere

TO USE GiiArchitect, you will need a .txt file that contains a list of titles (or some other list of text you want to create directories from).

If you are working with a project worksheet, you can create this .txt file by copying a selection of script titles into a new .txt file. Titles should be left-aligned and each title should exist on its own line. Pasting a single column of data from a spreadsheet into a text editor automatically formats the text correctly. Your text file should look something like this:

Title 1

Title 2 

Title 3 

Title 4 

etc.

Save your .txt file anywhere on your computer.

# Using GiiArchitect

1. When GiiArchitect runs, it will ask you to input the filepath where you would like the new directories to be created. 

2. When passed a legitimate filepath, GiiArchitect will request the filepath and extension of the .txt file where you have saved the script titles. 

3. When passed a legitimate .txt file, GiiArchitect will create a new, empty directory for each title saved in the .txt file. These new directories will be created in the parent directory specified by the user in step one.

# Limitations and Error Handling

1. The Windows operating system does not allow directory names to include the following characters: \/:*?"<>|
These illegal characters sometimes appear in our script titles. To handle illegal characters without crashing, GiiArchitect searches each title for illegal characters and removes them from the title. This creates some discrepancies between the directories that are created and the actual titles of the scripts. For example, a script titled:

"What is for Dinner?" "I Want Cake!"

Will create a directory named:

What is for Dinner I want Cake!

Illegal characters can be replaced with any character specified by the programmer. If an alternative replacement character is preferred, this can be addressed in a future iteration of GiiArchitect.

2. If asked to create a directory that already exists in the parent directory, GiiArchitect will return an error and return to the beginning of the script. Make sure all titles saved in your .txt file are unique before passing the .txt file to GiiArchitect.

3. When GiiArchitect is passed a filepath that does not make sense, it returns an error and returns to the beginning of the script.






GiiArchitect is on GitHub! https://github.com/twohundredboys/GiiArchitect

This file was last updated by:
Johnathan Ortiz-Sonnen on May 22, 2017
jsonnen89@gmail.org
