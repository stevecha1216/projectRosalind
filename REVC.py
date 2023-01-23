import fileoutput

#complement the dna
def complement(s):
    #turn dna string into a list
    dna = list(s)
    compdna = ""
    #iterate through the dna list and complement+add each base to comp
    for base in dna:
        if base == "A":
            compdna += "T"
        elif base == "T":
            compdna += "A"
        elif base == "G":
            compdna += "C"
        elif base == "C":
            compdna += "G"
    return(compdna)


#reverse the dna
def reverse(s):
    dna = list(s)
    revdna = ""
    for i in range(len(dna)-1, -1, -1):
        revdna += dna[i]
    return(revdna)


if __name__ == "__main__":
    s = input("Paste DNA string here\n")
    comp = complement(s)
    reversecomplement = reverse(comp)
    fileoutput.out(reversecomplement, "REVC")
    print(reversecomplement)
