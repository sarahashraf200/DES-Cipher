from Initials import *
from Functions import *
from Key import generateKey

def s(s_in, s_boxes):
    s_out = ""
    for i in range(8):
        j = i*6
        row = binToDec(s_in[j] + s_in[j+5])*16
        col = binToDec(s_in[j+1] + s_in[j+2] + s_in[j+3] + s_in[j+4])
        num = row + col
        s_out += decToBin(s_boxes[i][num]).zfill(4)
    return s_out

def f(plain, keys, i):
    P1 = permute(plain, EXPANSION)
    text = xor(P1, keys[i - 1])
    xorbox = s(text, s_boxes)
    P2 = permute(xorbox, P32)
    return P2

def encrypt(text, key):
    keys = generateKey(key)
    text = hexToBin(text)
    text = permute(text, IP)
    l_text, r_ight = divide(text)
    textLR = [l_text, r_ight]
    for i in range(1,17,1):
        textLR.append(textLR[i*2-1])
        textLR.append(xor(textLR[i*2-2], f(textLR[i*2-1], keys, i)))
    RL16=textLR[33] + textLR[32]
    return hex(int(permute(RL16, IP_I),2))[2:].upper().zfill(16)

def decrypt(text, key):
    keys = generateKey(key)[::-1]
    text = hexToBin(text)
    text = permute(text, IP)
    Ltext, Rtext = divide(text)
    textLR = [Ltext, Rtext]
    for i in range(1,17,1):
        textLR.append(textLR[i*2-1])
        textLR.append(xor(textLR[i*2-2], f(textLR[i*2-1], keys, i)))
    RL16=textLR[33] + textLR[32]
    return hex(int(permute(RL16, IP_I),2))[2:].upper().zfill(16)


if __name__== "__main__":


    Choice=input("Please enter E if you want encrypt or D if you want decrypt : ")
    Key = input("Please enter the key: ")
    NumberOfRuns = int(input("Please enter the round: "))

    if Choice=='E':
        PlainText=input("Please enter the Plain Text: ")


        for i in range(NumberOfRuns):
            r = encrypt(PlainText , Key)
            PlainText = r
        #cipheredText = encrypt(PlainText, Key)
        print("Ciphered Text: "+ r)
        input()

    elif Choice=='D':
        PlainText=input("Enter the encrypted Text: ")
        for i in range(NumberOfRuns):
            r = decrypt(PlainText , Key)
            PlainText = r

        print("Decrypted Text: "+ r)
        input()


