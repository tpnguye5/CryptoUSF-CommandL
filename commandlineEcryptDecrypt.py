import sys, getopt, math, random
import caesar, polyCipher, transposition, simpleSub

def main(argv, out, type, option):
    print("Hello, caesar cipher encrypt and decrypt is good. Polycipher is good. Simple and transposition can encrypt "
          "but cannot decrypt.")

    filename = ""
    output = ""

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if argv[1] == '-i':
        filename = argv[1]
    elif argv[2] == '-o':
        output = argv[2]
    elif argv[3] == 'ceasar':
        key = 3
        if argv[4] == '-e':
            test = caesar.caesarCipherENCRYPT(filename, output,key)
        elif argv[5] == '-d':
            test2 = caesar.caesarCipherDECRYPT(filename, output, key)

    elif argv[3] == 'simple':
        key_S = ''.join(random.sample(LETTERS, len(LETTERS)))
        if argv[4] == '-e':
            test3 = simpleSub.simple_sub_cipherENCRYPT(filename, output,key_S)
        elif argv[5] == '-d':
            test4= simpleSub.simple_sub_cipherDECRYPT(filename, output, key_S)

    elif argv[3] == 'poly':
        subkey = "SHIBA"
        if argv[4] == '-e':
            test5 = polyCipher.polyCipherENCRYPT(filename,output, subkey)
        elif argv[5] == '-d':
            test6 =polyCipher.polyCipherDECRYPT(filename, output, subkey)

    elif argv[3] == 'transposition':
        key_t = 6
        if argv[4] == '-e':
            test7 =transposition.transpositionENCRYPT(filename,output,key_t)
        elif argv[5] == 'd':
            test8 =transposition.transpositionDECRYPT(filename,output,key_t)

main('testFile.txt', 'result.txt','poly', '-e')



        # def main(input, output, flag_e, flag_d, cipher_type):
#     caesarkey = click.prompt("Enter integer for key: ", type=int)
#
#     if cipher_type == 'caesar' and flag_e == 'e':
#         test = caesar.caesarCipherENCRYPT(input, output, caesarkey)
#
#     elif cipher_type == 'caesar' and flag_d == 'd':
#         test2 = caesar.caesarCipherDECRYPT(input, output, caesarkey)
#
#     # elif cipher_type =='simple' and flag_e == 'e':
#     #     test3 = simple
#     # elif cipher_type == 'simple' and flag_d == 'd':
#     #     test4 =
#     # elif cipher_type =='polyalph' and flag_e == 'e':
#         test5 = polyCipher.polyCipherENCRYPT(input, output, key)
#     # elif cipher_type =='polyalph' and flag_d =='d':
#         # test6 = polyCipher.polyCipherDECRYPT(input, output, key)
#
#     # elif cipher_type == 'transposition' and flag_e =='e':
#         test7 = transposition.transpositionENCRYPT(input, output, key)
#     # elif cipher_type == 'transposition' and flag_d =='d':
#         # test8 =transposition.
#     else:
#         exit()
