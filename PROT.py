import fileinput as fi
import fileoutput as fo


def translate(rna):
    codontable = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "UAU":"Y",
              "UAC":"Y", "UAA":"","UAG":"", "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W", "CUU":"L", "CUC":"L",
              "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q",
              "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
              "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S",
              "AGC":"S", "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A",
              "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGU":"G", "GGC":"G", "GGA":"G",
              "GGG":"G"}
    #rna string to list to iterate through each base easier
    rna = list(rna)
    #codon placeholder
    codon = ""
    counter = 0
    #initialize codon list
    codonlist = []
    #iterate through rna to separate into codons
    for base in rna:
        if counter < 3:
            codon += base
            counter += 1
            if len(codon) == 3:
                codonlist.append(codon)
        else:
            counter = 1
            #print(codon)
            codon = str(base)
    protein = ""
    for codon in codonlist:
        protein += codontable[codon]
    # print(rna)
    # print(codonlist)
    return(protein)


if __name__ == "__main__":
    # filename = "prot_test"
    filename = "rosalind_prot"
    datain = fi.readinput(filename)
    #print(translate(datain))
    output = translate(datain)
    fo.out(output, "PROT")
