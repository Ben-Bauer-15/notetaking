from time import *


def appendText(text):
    f = open('notes.md', "a")
    f.write(text)
    f.close()

def sleepAppendText():
    date = 10
    while True:
        appendText('\n ### 1/' + str(date) + '/19')
        appendText('\n')
        appendText('\n worked on the hangman app')
        appendText('\n')
        appendText('\n')
        date += 1
        sleep(5)

sleepAppendText()


# python -u "/Users/bbauer/Desktop/notes/write.py"


#         git add notes.md
#         git commit -m 'latest changes'
#         git push

