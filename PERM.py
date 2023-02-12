import fileoutput as fo
import fileinput as fi


def permutations(n):
    n = int(n)
    permlist = []
    permlist.extend(range(1, n+1))
    permlist = list(map(str, permlist))
    permlist = createperms(permlist)
    out = str(len(permlist)) + "\n"
    for p in permlist:
        for digit in p:
            out += digit + " "
        out = out[:-1]
        out += "\n"
    out = out[:-1]
    return(out)


# Python function to print permutations of a given list
def createperms(permlist):
    if len(permlist) == 1:
        return [permlist]
    outlist = []
    for i in range(len(permlist)):
        x = permlist[i]
        y = permlist[:i] + permlist[i + 1:]
        for p in createperms(y):
            outlist.append([x] + p)
    return (outlist)


if __name__ == "__main__":
    # change filename
    # filename = "perm_test"
    filename = "rosalind_perm"

    # keep this the same
    datain = fi.readinput(filename)

    permutations(datain)
    # change the function name
    output = permutations(datain)
    # change the output file name
    fo.out(output, "PERM")
