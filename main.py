from easygui import choicebox, fileopenbox
import os, sys, csv

# setting up required fields for the choicebox
msg = ("Welcome to Nyx Browser!\n\nNyx is an application designed to group all important "
       "files together for convenient access.\n\n\nSelect an action to do or a file to open.")
title = "Nyx v1.0"
choices = []

# creating the main choices list and initializing empty lists for displaying files in proglist.csv
files = []
files_fixed = []


# loads proglist.csv, reads file and adds them to files list



# defining function to add file to browser view
def add_file():
    new = fileopenbox()
    with open('proglist.csv', 'a+') as file:
        file.write(new + '\n')
    lobby()


# defining function to remove file from browser view
def remove_file():
    msg_r = "Which file would you like to remove?"
    title_r = "Remove File from Browser"
    choices_r = files_fixed

    if "> Back" in choices_r:
        pass
    else:
        choices_r.append("> Back")

    choice_r = choicebox(msg_r, title_r, choices_r)

    if choice_r == "> Back":
        return lobby()
    else:
        files_fixed.pop(files_fixed.index(choice_r))
        files_fixed.pop(files_fixed.index("> Back"))
        with open('proglist.csv', 'w') as nf:
            for file in files_fixed:
                nf.write(file + "\n")
    lobby()

def csv_load():
    with open('proglist.csv', '+r') as f:
        reader = csv.reader(f, delimiter="\n")
        [files.append(line) for i, line in enumerate(reader)]


# defining main function that displays browser menu
def lobby():
    csv_load()

    choices = ["> Add file to Nyx Browser", "> Remove file from Nyx Browser"]
    
    #
    for i in range(len(files)):
        files_fixed.append(files[i][0])

    for f in files_fixed:
        choices.append("{}".format(f))
    
    #
    choices.append("> Exit")

    csv_load()
    choice = choicebox(msg, title, choices)

    
    for c in choices:
        if choice == "> Add file to Nyx Browser":
            return add_file()
        elif choice == "> Remove file from Nyx Browser":
            return remove_file()
        elif choice == "> Exit":
            sys.exit(0)
        else:
            os.startfile(choice)
            return lobby()


# program start
if __name__ == "__main__":
    lobby()