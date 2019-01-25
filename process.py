import sys
date = sys.argv[1]


def addToFile():
    f = open("notes.md", "a")
    f.write("\n\n ### 1/"+ str(date) +"/19 \n worked on the hangman app")


addToFile()
