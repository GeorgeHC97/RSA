from speedyfunctions import fast, egcd, modinv
from math import gcd

def pospair(c): #Return the line,position pair assosciated with char c
    for i in range(0, lenKey): #loop through the lines of the key
        if c in linesKey[i]: #if c appears in the line
            linesKey[i].index(c)
            return [i,linesKey[i].index(c)]
    return 0

def encrypt(i,e,n): #i^e mod n encryption
    return pow(i,e,n)

def decrypt(j,d,n): #use modular inverse of e to decrypt
    return pow(j,d,n)


#Read Input File
file = open("code.param","r")

lines = file.readlines()
#Read first line containing 3 ints: p,q,e
numbers = [int(n) for n in lines[0].split()]
if len(numbers) != 3:
    raise Exception("Input File Error - First line")
p,q,e = numbers

#read file named in second line of Input File: string to be encoded
fileinput1 = open(lines[1].rstrip('\n'),"r")
code = fileinput1.read()
fileinput1.close()

#read file named in third line of Input file: string to be used as encoding key
fileinput2 = open(lines[2].rstrip('\n'),"r")
linesKey = fileinput2.readlines()
lenKey = len(linesKey)
fileinput2.close()

file.close()






######################################
##      RSA ALGORITHM               ##
######################################
#Large Primes
#p = 1300051
#q = 17
#Product of Large Primes
n = p * q
#Euler totient
phi = n - p - q + 1 #=(p1-1)(p2-1)
#print(phi)

d = modinv(e,phi)
########################################

#Turn codetext into pairs of positions in keytext


positions = []
for c in code: #loop through characters and put their position pairs in a list
    positions.append(pospair(c))
#print(positions)


encryptedpos = []
for i in positions: #loop through positions and encrypt them
    temp = []
    for j in i:
        temp.append(encrypt(j,e,n))
    encryptedpos.append(temp)

#print(encryptedpos)

fileoutput = open("code.out","w")

#Write the encrypted positions to the file
for i in encryptedpos:
    fileoutput.write(str(i) + "\n")
print("Done")
fileoutput.close()




