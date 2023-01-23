def transcribe(t):
    DNA = list(t)
    RNA = ""
    for nuc in DNA:
        if nuc == "T":
            RNA += "U"
        else:
            RNA += nuc
    return(RNA)

if __name__ == "__main__":
    t = input("Paste DNA string here\n")
    print(transcribe(t))