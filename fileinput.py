import os


def readinput(filename):
    os.chdir("infiles")
    file = filename + ".txt"
    filein = open(file, "r")
    textin = filein.read()
    os.chdir("..")
    return(textin)
