from speedyfunctions import fast,egcd,modinv
import random
from math import gcd

def decrypt(j,d,n):
    return pow(j,d,n)

#pollard rho algorithm
def PollardRho(n):
    #using f(x) = x^2 + c

    #if n is even return 2
    if n%2==0:
        return 2

    #pick random integers between 1 and n - 1
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    factor = 1

    #when factor > 1 then factor is a prime factor of n
    while factor==1:
            x = ((x*x) % n + c) % n
            y = ((y*y) % n + c) % n
            y = ((y*y) % n + c) % n
            factor = gcd(abs(x-y), n)

    return factor


#Values given for the task
n = 32193613398841823
e = 17

#open file with encrypted positions
fileinput = open("madrigal.code","r")
lines = fileinput.readlines()
#read posiitons into a list
encryptedpos = []
for i in lines:
    numbers = [int(n) for n in i.split()]
    encryptedpos.append(numbers)
#print(encryptedpos)
#close file
fileinput.close()

#open KublaKhan.txt as keytext
fileinput = open("KublaKhan.txt","r")
keytext = fileinput.readlines()
fileinput.close()

#Pollar Rho Integer Factorization Algorithm
#find d and phi
p = PollardRho(n)
q = int(n/p)
phi = n - p - q + 1
d = modinv(e,phi)
#print(modinv(d,phi) == e)

#decrypt the encrypted positions
decryptedpos = []
for i in encryptedpos:
    temp = []
    for j in i:
        temp.append(decrypt(j,d,n))
    decryptedpos.append(temp)


#recreate the text using the keytext
text = ""
errors = []
for pos in decryptedpos:
    try:
        text = text + keytext[pos[0]][pos[1]]
    except IndexError:
        text = text
        errors.append(pos)
#print(text)

#Write the reconstructed text to a file called madrigal.out
fileoutput = open("madrigal.out","w")
fileoutput.write(text)
fileoutput.close()
print("Done")

print(text)
