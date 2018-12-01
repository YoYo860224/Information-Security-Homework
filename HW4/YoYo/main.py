import sys
import RSA
import RandPrime
import random

def printUsage():
    print('Please input Hex.')
    print('Usage: -init')
    print('Usage: -init <NumOfBit>')
    print('Usage: -init <prime1> <prime2>')
    print('Usage: -e <plaintext> <N> <key>')
    print('Usage: -e <plaintext> <N> <key> <p> <q>')
    print('Usage: -d <ciphertext> <N> <key>')
    print('Usage: -d <ciphertext> <N> <key> <p> <q>')

def main():
    if len(sys.argv) < 2:
        printUsage()
        return
    
    if sys.argv[1] == '-init':
        p = 0
        q = 0
        N = 0
        e = 0
        d = 0
        if len(sys.argv) == 2:
            N, e, d, p, q = RSA.GetRSAKeyByBit(1024)
        if len(sys.argv) == 3:
            N, e, d, p, q = RSA.GetRSAKeyByBit(int(sys.argv[2]))
        if len(sys.argv) == 4:
            p = int(sys.argv[2], 16)
            q = int(sys.argv[3], 16)
            N, e, d = RSA.GetRSAKeyByPrime(p, q)
        print()
        print('p = ', hex(p))
        print('q = ', hex(q))
        print('N = ', hex(N))
        print('Public  Key = ', hex(e))
        print('Private Key = ', hex(d))
    elif sys.argv[1] == '-e' or sys.argv[1] == '-d':
        if len(sys.argv) == 5:
            message = int(sys.argv[2], 16)
            N = int(sys.argv[3], 16)
            k = int(sys.argv[4], 16)
            getMessage = RSA.RSA(message, N, k)
            print()
            print(hex(getMessage))
        elif len(sys.argv) == 7:
            message = int(sys.argv[2], 16)
            N = int(sys.argv[3], 16)
            k = int(sys.argv[4], 16)
            p = int(sys.argv[5], 16)
            q = int(sys.argv[6], 16)
            getMessage = RSA.RSAbyCRT(message, N, k, p, q)
            print()
            print(hex(getMessage))
        else:
            printUsage()
            return
    else:
        printUsage()
        return
    
if __name__ == "__main__":
    main()
