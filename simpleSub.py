#attbash
import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = ''.join(random.sample(LETTERS, len(LETTERS)))

##############################################################################################
#Another simple substitution cipher
#Page 15 in the "Manual of Cyptography".
#single alphabet cipher, sliding cipher

def simple_sub_cipherENCRYPT(infile, outfile, key):
    #no key will be needed. Loop through the text and place words in array
    #Then, make array into one string. This is our key. Must
    print('function')
    translate =""


    #take file, open file
    file = open(infile, 'r')
    #loop through the file
    for line in file:
        line = line.strip().upper()
        print(line)
        for ch in line:
            if ch in LETTERS:
            #cipher the character and add charcter in translate
                chIndex = LETTERS.find(ch)
                translate += key[chIndex].upper()
            if ord(ch) == 32:
                translate += " "

    print(translate)
    out = open(outfile, 'w')
    out.write(translate)
    out.close()

def simple_sub_cipherDECRYPT(infile, outfile, key):
    translate = ""

    # take file, open file
    file = open(infile, 'r')
    # loop through the file
    for line in file:
        line = line.strip().upper()
        print(line)
        for ch in line:
            if ch in key:
                #get ord value
                val = ord(ch)
                print (val)
                #loop through letters and find which other letter has same ord value
                #convert back and sappend in translate

                for i in range(len(LETTERS)-1):
                    if ord(LETTERS[i]) == val:
                        translate += chr(val).upper()
                        print(translate)
                    # print(l, ord(l))
                    # if ord(l) == val:

            if ord(ch) == 32:
                translate += " "

                # cipher the character and add charcter in translate
            #     chIndex = key.find(ch)
            #
            #     translate += LETTERS[chIndex].upper()
            # if ord(ch) == 32:
            #     translate += " "

    print(translate)
    out = open(outfile, 'w')
    out.write(translate)
    out.close()

# def isKeyValid(key):
#     #make key letters into list
#     keyList = list(key)
#     #make list of lettes
#     letters = list(LETTERS)
#     #sort the key list and letter list
#     keyList = keyList.sort()
#     letters = letters.sort()
#     #go through list and
#     # check if characters in key list are the same as characters in letters
#     if keyList != letters:
#         sys.exit('Error with key')

#
# def main():
#     print('ji')
#     print(key)
#     # simple_sub_cipherENCRYPT('testFile.txt','result.txt', key)
#     simple_sub_cipherDECRYPT('result.txt', 'testFile.txt', key)
#     print("lo")
#
# main()