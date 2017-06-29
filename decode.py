from speedyfunctions import egcd,fast,modinv



def decrypt(j,d,n):
    return pow(j,d,n)

#Read Input File
file = open("decode.param","r")

lines = file.readlines()
#Read first line containing 3 ints: p,q,e
numbers = [int(n) for n in lines[0].split()]
if len(numbers) != 3:
    raise Exception("Input File Error - First line")
p,q,e = numbers

#Product of Large Primes
n = p * q
#Euler totient
phi = n - p - q + 1 #=(p1-1)(p2-1)
#multi inv
d = modinv(e,phi)

#read file named in second line of Input File: encrypted positions to be decoded
fileinput1 = open(lines[1].rstrip('\n'),"r")
lines1 = fileinput1.readlines()
fileinput1.close()

#Read the encrypted positions into a list
encryptedpos = []
for i in lines1:
    encryptedpos.append(eval(i.rstrip("\n")))
#print(encryptedpos)
fileinput1.close()

#Read the lines from key text
fileinput2 = open(lines[2].rstrip("\n"))
lines2 = fileinput2.readlines()
fileinput2.close()

file.close() #close decode.param


#decrypt the positions
decryptedpos = []
for i in encryptedpos:
    temp = []
    for j in i:
        temp.append(decrypt(j,d,n))
    decryptedpos.append(temp)

#recreate the original text using the key text)
text = ""
for pos in decryptedpos:
    text = text + lines2[pos[0]][pos[1]]

fileoutput = open("decode.out","w")
fileoutput.write(text)
fileoutput.close()
print("Done")