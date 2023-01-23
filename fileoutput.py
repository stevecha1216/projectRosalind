import os


def out(answer, problemID):
    answer = str(answer)
    os.chdir("outfiles")
    filename = problemID + "_out.txt"
    file = open(filename, "w")
    file.write(answer)
    file.close()
