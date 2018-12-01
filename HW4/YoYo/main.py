import sys
import RSA
import RandPrime
import random

def printUsage():
    print('Usage: -init')
    print('Usage: -e <plaintext> <N> <key>')
    print('Usage: -e <plaintext> <N> <key> <p> <q>')
    print('Usage: -d <ciphertext> <N> <key>')
    print('Usage: -d <ciphertext> <N> <key> <p> <q>')

def main():
    if len(sys.argv) < 2:
        printUsage()
        return
    
    if sys.argv[1] == '-init':
        p = RandPrime.RandomPrime(512)
        q = RandPrime.RandomPrime(513)
        while(p == q):
            q = RandPrime.RandomPrime(10)
        N, e, d = RSA.GetRSAKey(p, q)
        print('p = ', p)
        print('q = ', q)
        print('N = ', N)
        print('Private Key = ', e)
        print('Public  Key = ', d)
    elif sys.argv[1] == '-e' or sys.argv[1] == '-d':
        if len(sys.argv) == 5:
            message = int(sys.argv[2])
            N = int(sys.argv[3])
            key = int(sys.argv[4])
            getMessage = RSA.RSA(message, N, key)
            print(getMessage)
        elif len(sys.argv) == 7:
            message = int(sys.argv[2])
            N = int(sys.argv[3])
            key = int(sys.argv[4])
            getMessage = RSA.RSA(message, N, key)
            print(getMessage)
        else:
            printUsage()
            return
    else:
        printUsage()
        return
    
if __name__ == "__main__":
    main()
