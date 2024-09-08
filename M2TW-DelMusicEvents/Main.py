import sys
import pathlib
import os

def Main():
    if(pathlib.Path(str(os.getcwd() + "\\data\\sounds")).exists()):
        os.remove(str(os.getcwd() + "\\data\\sounds\\events.dat"))
        os.remove(str(os.getcwd() + "\\data\\sounds\\events.idx"))
        os.remove(str(os.getcwd() + "\\data\\sounds\\Music.dat"))
        os.remove(str(os.getcwd() + "\\data\\sounds\\Music.idx"))
    else:
        print("This Script is not Detected M2TW Dir or Mod Folder...")
        exit(443)

if __name__ == "__main__":
    Main()