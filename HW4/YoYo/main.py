import sys
import RSA
import RandPrime
import random

def printUsage():
    print('Please input Decimal.')
    print('Usage: -init')
    print('Usage: -init <NumOfBit>')
    print('Usage: -e <plaintext> <N> <key>')
    print('Usage: -e <plaintext> <N> <key> <p> <q>')
    print('Usage: -d <ciphertext> <N> <key>')
    print('Usage: -d <ciphertext> <N> <key> <p> <q>')

def main():
    if len(sys.argv) < 2:
        printUsage()
        return
    
    if sys.argv[1] == '-init':
        needBits = 1024
        if len(sys.argv) == 3:
            needBits = int(sys.argv[2])
        N, e, d, p, q = RSA.GetRSAKeyByBit(needBits)
        print()
        print('p = ', p)
        print('q = ', q)
        print('N = ', N)
        print('Public  Key = ', e)
        print('Private Key = ', d)
    elif sys.argv[1] == '-e' or sys.argv[1] == '-d':
        if len(sys.argv) == 5:
            message = int(sys.argv[2])
            N = int(sys.argv[3])
            k = int(sys.argv[4])
            getMessage = RSA.RSA(message, N, k)
            print()
            print(getMessage)
        elif len(sys.argv) == 7:
            message = int(sys.argv[2])
            N = int(sys.argv[3])
            k = int(sys.argv[4])
            p = int(sys.argv[5])
            q = int(sys.argv[6])
            getMessage = RSA.RSAbyCRT(message, N, k, p, q)
            print()
            print(getMessage)
        else:
            printUsage()
            return
    else:
        printUsage()
        return
    
if __name__ == "__main__":
    main()
