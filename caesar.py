#Caesar Cipiher Function. Takes a file, converts everything to uppercase, performs,
#result in output file

# Listing every possible symbol that can be encrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesarCipherENCRYPT(fileName, outFile, key):
    #opens file from parameter
    file = open(fileName, "r")
    outfile = open(outFile, "w")
    #moving through each line
    for line in file:
        print(line)
        for l in line.upper():
            if l in LETTERS:
                index = (LETTERS.index(l) + key) % 26
                outfile.write(LETTERS[index])
            if ord(l) == 32:
                outfile.write(" ")
    file.close()
    outfile.close()

def caesarCipherDECRYPT(fileName, outFile, key):
    # opens file from parameter
    file = open(fileName, "r")
    outfile = open(outFile, "w")

    # moving through each line
    for line in file:
        for l in line.upper():
            if l in LETTERS:
                index = (LETTERS.index(l) - key) % 26
                outfile.write(LETTERS[index])
            if ord(l) == 32:
                outfile.write(" ")
    file.close()
    outfile.close()

