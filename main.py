from easygui import choicebox, fileopenbox
import os, sys, csv

msg = ("Welcome to Nyx!\n\nNyx is an application designed to group all important "
       "files together for convenient access.\n\n\nSelect an action to do.")
title = "Nyx v1.0"
choices = ["> Add file to Nyx browser",
           "> Exit"]



def add_file():
    new = fileopenbox()
    with open('proglist.csv', 'a+') as file:
        file.write(new + '\n')
    return lobby()

def lobby():
    choice = choicebox(msg, title, choices)

    if choice == choices[0]:
        return add_file()
    else:
        return 0
        #sys.exit(0)

if __name__ == "__main__":
    lobby()