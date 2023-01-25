import os
import fileinput as fi
import fileoutput as fo


def hammingdistance(data):
    dna = data.split("\n")
    #print(dna)
    strandone = dna[0]
    strandtwo = dna[1]
    hammdist = 0
    for i in range(0, len(strandone)):
        if strandone[i] != strandtwo[i]:
            hammdist += 1
    return(hammdist)

if __name__ == "__main__":
    #filename = "hamm_test"
    filename = "rosalind_hamm"
    datain = fi.readinput(filename)
    output = hammingdistance(datain)
    #print(output)
    fo.out(output, "HAMM")