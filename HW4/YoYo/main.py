import sys
import RSA
import RandPrime

def main():
    # p = 71
    # q = 83
    p = RandPrime.RandomPrime()
    q = RandPrime.RandomPrime()
    print(p, q)
    N, e, d = RSA.GetRSAKey(p, q)
    print(N.bit_length())

    message = 2018
    en = RSA.RSA(message, N, e)
    print(en)
    de = RSA.RSA(en, N, d)
    print(de)
    
if __name__ == "__main__":
    main()
