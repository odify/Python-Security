#!/usr/bin/env python3

from random import choice, randint
from math import gcd,pow
import os
import datetime
import pyfiglet


result = pyfiglet.figlet_format("RSA-Crytor")
print(result)
print("\n") # describtion-row

os.system("date")
#--------------
def IsPrimeNumber(num):
    flag = 0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if(flag==0) and (num!=1):
        return num


def GenerateLargeRandomPrime():
    PrimeNum = []
    for i in range(0,100):
        randomNum = list(range(1,1000))
        #call
        Prime = IsPrimeNumber(choice(randomNum))
        if Prime != None:
            PrimeNum.append(Prime)
    return PrimeNum 


def KeyGeneration():

    PrimeNumber = GenerateLargeRandomPrime()
    PrimeList = []
    for ii in PrimeNumber:
        #Because last value of ASCII is 127, as some times the ASCII value of the plaintext character exceeds N, and when we decrypt the ciphertext , it will not reproduce the plaintext
        if ii > 127:
            PrimeList.append(ii)

    #Bob chooses two large prime numbers p and q
    p = choice(PrimeList)
    q = choice(PrimeList)

    #Bob computes N = p*q
    N = p*q
    
    #Bob computes another number phi = (p-1)*(q-1)
    phi = (p-1)*(q-1)
    
    print("p = ",p)
    print("q = ",q)
    print("N = ",N)
    print("phi = ",phi)

    #Bob chooses random integer 'e' less than N, such that 'e' and 'phi' are relative prime 
    # =====> gcd(e,phi) = 1
    for i in range(1,N):
        if (i<N) and (gcd(i,phi)==1):
            E = []
            E.append(i)
    e = choice(E)
    for i in range(1,N):
        d=i
        #choose 'd' such that (e*d) mod (phi) = 1
        if ((e*d)%phi) == 1:
            D = []
            D.append(d)
            d = choice(D)
            print("e = ",e)
            print("d = ",d)
            #Bob announces 'e' and 'N' to public, he keeps 'phi' and 'd' secret
            return e,d,N


e,d,N = KeyGeneration()

def RSA_Encryption(p,e,N):
    print("Public Key = ({},{})".format(N,e))
    PT_encode = []
    CT = []

    #This will give the ASCII value of the each character of the plaintext and store in the PT_encode[] list
    for i in p:
        PT_encode.append(ord(i))
    print("Plaintext (in ASCII) = ", PT_encode)

    #From PT_encode[] list, retrieve one by one element and compute cipher (in ASCII form), and store the result of each in the CT[] list i.e. CT[] will keep track of all the ciphertext formed by plaintext (in ASCII form)
    for P in PT_encode:
        CT.append((P**e) % N)
    print("Encryption of plaintext (in ASCII) = ",CT)

    #change the ASCII form number to character form
    """
    cipherText = []
    for j in CT:
        cipherText.append(chr(j))
    print("Ciphertext = ",cipherText)
    """
    return CT


plaintext = input("Enter the message you want to encrypt : ")
print("Plaintext = ", plaintext)

ciphertext = RSA_Encryption(plaintext, e,N)

def RSA_Decryption(c,d,N):
    print("Private Key = ({},{})".format(N,d))

    #PT[] list will keep track of all the plaintext character letter code (in ASCII)
    PT = []
    #retrieve each character from "c" list (ciphertext) and compute corresponding plaintext and store each result in PT[] list (in ASCII form)
    for C in c:
        PT.append((C**d) % N)
        
    print("Decryption of ciphertext (in ASCII) = ",PT)
    
    #plaintext[] list stores the character (alphabet) of the each digits from the PT[] list
    plainText = []
    #This will convert the ASCII number of the plaintext into character (alphabet)
    for j in PT:
        plainText.append(chr(j))

    #combine each alphabet of the plainText[] list into one single string
    print("Plaintext = ","".join(plainText))
    return plainText 

P = RSA_Decryption(ciphertext,d,N)
