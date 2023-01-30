import fileinput as fi
import fileoutput as fo


def gccontentfinder(datain):
    fastalist = datain.split(">Rosalind_")
    fastalist.pop(0)
    #print(fastalist)
    id = ""
    gc = 0
    length = 0
    idgc = []
    for data in fastalist:
        #print(data)
        sequence = list(data)
        for c in sequence:
            #print(c)
            if c == "C" or c == "G":
                gc += 1
                length += 1
            elif c == "A" or c == "T":
                length += 1
            elif c.isnumeric():
                id += c
        #print(gc)
        # print(length)
        gccontent = (gc/length)*100
        idgc.append((id,gccontent))
        gc = 0
        length = 0
        id = ""
    # print(idgc)
    greatestindex = 0
    for dataset in idgc:
        if dataset[1] > idgc[greatestindex][1]:
            greatestindex = idgc.index(dataset)

    out = "Rosalind_" + str(idgc[greatestindex][0]) + "\n" + str(idgc[greatestindex][1])
    # print(greatestindex)
    # print(out)
    return(out)


if __name__ == "__main__":
    # filename = "gc_test"
    filename = "rosalind_gc"
    datain = fi.readinput(filename)
    output = gccontentfinder(datain)
    fo.out(output, "GC")
