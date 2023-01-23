import os
import fileoutput as fo
import fileinput as fi


def rabbits(months_offspring):
    months_offspring = months_offspring.split()
    months = int(months_offspring[0])
    offspring = int(months_offspring[1])
    adultpairs = 0
    growingpairs = 1
    childpairs = 0
    for i in range (0,months):
        growingpairs += childpairs
        childpairs = adultpairs * offspring
        adultpairs += growingpairs
        growingpairs = 0
    rabbitcount = adultpairs + growingpairs
    return(rabbitcount)


if __name__ == "__main__":
    #filename = "fib_test"
    filename = "rosalind_fib"
    datain = fi.readinput(filename)
    output = rabbits(datain)
    fo.out(output, "FIB")
