##############################################################################################
#A transposition cipher
#This cipher is more secure as it had many more possible keys to make a brute force attack more
#difficult.
#Federal Army Cipher
#In this cipher, letters are not altered, but their order is changed.
import math
def transpositionENCRYPT(fileName, outFile, key):
    file = open(fileName, "r")
    messge = ""
    for line in file:
        messge += line + " "

    text = ['']* key
    #our key will represent the number of columns needed
    #Count the number of characters in the file
    #Fill in the array
    #When you run out of boxes, add another row of boxes

    #open file and read

    for col in range(key):

        pointer = col

        while pointer < len(messge):
            text[col] += messge[pointer]
            pointer += key
    file.close()
    outfile = open(outFile, 'w')
    finaltext = ""
    for charac in text:
        finaltext += charac
    # finaltext = "".join(text)
    outfile.write(finaltext)
    outfile.close()

def transpositionDECRYPT(filename, outfile, key):
    file = open(filename, "r")
    text = ""

    for line in file:
        text += line + " "

    numCol = math.ceil(len(text)/key)
    numrows = key
    badBoxes = (numCol * numrows) - len(text)

    result = [''] * numCol

    col =0
    row =0

    for ch in text:
        result[col] += ch
        col += 1
        if col == numCol or (col== numCol -1 and row >= numrows-badBoxes):
            col = 0
            row += 1
    out = open(outfile, 'w')
    final = ""
    for let in result:
        final += let

    print(final)
    out.write(final)
    out.close()
    # return ''.join(result)

# def main():
#     key = 3
#     # transpositionENCRYPT('testFile.txt','result.txt', key)
#     transpositionDECRYPT('result.txt', 'testFile.txt', key)
# main()