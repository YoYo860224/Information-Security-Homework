import sys
import RSA
import RandPrime
import random

def main():
    # p = 71
    # q = 83
    p = RandPrime.RandomPrime(255)
    q = RandPrime.RandomPrime(256)
    while(p == q):
        q = RandPrime.RandomPrime(10)
    print(p, q)
    N, e, d = RSA.GetRSAKey(p, q)
    print(N.bit_length())

    message = 1024
    en = RSA.RSA(message, N, e)
    print(en)
    de = RSA.RSA(en, N, d)
    print(de)
    
if __name__ == "__main__":
    main()
