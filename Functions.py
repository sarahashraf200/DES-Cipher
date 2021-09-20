def hexToBin(str):
    scale = 16
    return  ( bin(int(str, scale))[2:] ).zfill(len(str)*4)

def permute(str, P):
    block = ""
    for i in range(len(P)):
        block += str[P[i]-1]
    return block

def divide(s):
    return s[:(len(s)//2)] , s[len(s)//2:]

def xor(a, b):
    c = ""
    for i in range(len(a)):
        c += str(int(a[i]) ^ int(b[i]))
    return c

def binToDec(n):
    res = 0
    for i in range(len(n) - 1, -1, -1):
        if n[i]=='1':
            res = res + pow(2, abs(i - (len(n) - 1)))
    return res

def decToBin(i):
    x= ""
    while(i>0):
        if i%2:
            x += '1'
        else:
            x+='0'
        i //= 2
    return x[::-1]
