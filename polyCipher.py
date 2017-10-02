##############################################################################################
#A poly-alphabetic cipher
#Vigenere cipher
#single word key will be split into multiple subkeys
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def polyCipherENCRYPT(file,outfile,subkey):
    result = []  #Where we store the final message

    key_index = 0
    key = subkey.upper()

    #loop through each char in file
    file = open(file, 'r')
    for line in file:
        for ch in line:
            #get index number
            index = LETTERS.find(ch.upper())
            if index != -1: #if index is not -1, which means the ch is not in LETTERS
                index += LETTERS.find(key[key_index])
                index =index %len(LETTERS) #creates wrap
                # print("chnge:" ,index)
                result.append(LETTERS[index]) #new index
                key_index += 1 #next character in subkey
                if key_index == len(key):
                    #set key index back to 0
                    key_index = 0
            else:
                result.append(ch) #This is for punctuation marks

    file.close()
    out = open(outfile, 'w')
    final = ""
    for let in result:
        final += let

    print("encrypt:",final)

    out.write(final)
    out.close()

def polyCipherDECRYPT(file, outfile, subkey):
    result = []
    key_index = 0
    key = subkey.upper()

    # loop through each char in file
    file = open(file, 'r')
    for line in file:
        for ch in line:
            # get index number
            index = LETTERS.find(ch.upper())
            if index != -1:  # if index is not -1, which means the ch is not in LETTERS
               #Subtract for decrypting
                index -= LETTERS.find(key[key_index])

                index = index % len(LETTERS)  # creates wrap

                result.append(LETTERS[index])  # new index

                key_index += 1  # next character in subkey
                if key_index == len(key):
                    # set key index back to 0
                    key_index = 0
            else:
                result.append(ch)  # This is for punctuation marks

    out = open(outfile, 'w')
    final = ""
    for let in result:
        final += let
    out.write(final)
    out.close()
#
# def main():
#     subkey = "SHIBA"
#     print(subkey)
#     polyCipherENCRYPT('testFile.txt', 'result.txt', subkey)
#     polyCipherDECRYPT('testFile.txt','result.txt', subkey)
#
# main()