import fileinput as fi
import fileoutput as fo

def nucCount(s):
    s = list(s)
    #print(s)
    a,t,g,c = 0,0,0,0
    for nuc in s:
        if nuc == "A":
            a += 1
        elif nuc == "T":
            t += 1
        elif nuc == "G":
            g += 1
        elif nuc == "C":
            c += 1
    out = str(a) + " " + str(c) + " " + str(g) + " " + str(t)
    #print(out)
    return(out)



if __name__ == "__main__":
    #change filename
    #filename = "dna_test"
    filename = "rosalind_dna"

    #keep this the same
    datain = fi.readinput(filename)

    #change the function name
    output = nucCount(datain)
    #change the output file name
    fo.out(output, "DNA")
