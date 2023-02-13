import fileinput as fi
import fileoutput as fo


def motif(data):
    d = data.split("\n")
    #print(d)
    dna, sub = d[0], d[1]
    #print(dna,sub)
    dna = list(dna)

    temp = ""
    out = ""

    # loop through DNA string
    # if the current base == first base in the substring, build the string "temp" with the next bases of dna[i]
    # build "temp" to be the same length as the substring, then compare the two
    # make sure to reset temp after every base
    for i in range(len(dna)):
        if dna[i] == sub[0]:
            for j in range(0, len(sub)):
                if i+j < len(dna):
                    temp += dna[i+j]
                # print(temp)
            if temp == sub:
                out += str(i+1) + "  "
        temp = ""

    # shave off the space at the end
    out = out[:-2]
    return(out)


if __name__ == "__main__":
    # change filename
    #filename = "subs_test"
    filename = "rosalind_subs"

    # keep this the same
    datain = fi.readinput(filename)

    # change the function name
    output = motif(datain)
    # change the output file name
    fo.out(output, "SUBS")