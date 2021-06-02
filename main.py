import os
import shutil

"""
Sorts the downloads folder according to extension

Uses the os library for managing directories and files
Uses the shutil library for moving files

Started on 4/10/2021, 12:10 PM
Finished on 4/10/2021, 13:00 PM

"""

# Look through directory
# Check if directory has needed sub-directories
# If it does, move unsorted files in the directory to its specified sub-directories
# If it doesn't, create the required sub-directories and then sort the files into said sub-directories

extensions = [".png", ".jpeg", ".jpg", ".exe", ".ttf", ".pdf"]


def lookThroughDirectory():
    files = os.listdir()
    for file in files:
        if not file.__contains__("."):
            continue
        extension = os.path.splitext(file)[1]
        if extension not in extensions:
            sort("OtherStuff", file)
        elif extension == ".jpg" or extension == ".png" or extension == ".jpeg":
            sort("TempFiles", file)
        elif extension == ".exe":
            sort("Apps", file)
        elif extension == ".ttf":
            sort("Fonts", file)
        elif extension == ".pdf":
            sort("PDFs", file)


def sort(name, file):
    try:
        if os.path.exists(name):
            shutil.move(file, name)
        elif not os.path.exists(name):
            os.mkdir(name)
            shutil.move(file, name)
        else:
            print("Unmet condition")
    except:
        pass


if __name__ == "__main__":
    os.chdir(r"C:\Users\danie\Downloads")
    lookThroughDirectory()
    print("Completed")
