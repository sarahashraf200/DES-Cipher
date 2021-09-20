from Initials import *
from Functions import *

def shift(s, bit, mode):
    x = ""
    if mode == 0:
        x = (s * 3)[len(s) + bit: 2 * len(s) + bit]
    else:
        x = (s * 3)[len(s) - bit: 2 * len(s) - bit]
    return x

def generateKey(key):
    key = hexToBin(key)
    key56 = permute(key, PC1)
    Lkey,Rkey = divide(key56)
    keysLR = [Lkey, Rkey]
    for i in range(16):
        keysLR.append(shift(keysLR[i*2], LSH[i], 0))
        keysLR.append(shift(keysLR[(i*2)+1], LSH[i], 0))

    keys =[]
    for i in range(2, len(keysLR), 2):
        keys.append(keysLR[i]+keysLR[i+1])

    keys48 = []
    for i in range(len(keys)):
        temp = permute(keys[i], PC2)
        keys48.append(temp)

    return keys48