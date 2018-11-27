import sys
from RSA import RSA
from BigPrime import BigPrime


def printHint():
    print('Usage: -e <plaintext>')
    print('Usage: -e <plaintext> <n> <public key>')
    print('Usage: -e <plaintext> <prime p> <prime q> <public key>')
    print()
    print('Usage: -d <ciphertext> <n> <private key>')
    print('Usage: -d <ciphertext> <prime p> <prime q> <private key>')


def main():
    if len(sys.argv) < 3:
        printHint()
        return

    deOrEn = sys.argv[1]
    text = sys.argv[2]
    text = int(text, 16) if text[0:2].lower() == '0x' else int(text)

    if len(sys.argv) == 3:
        if deOrEn == '-e':
            p = BigPrime.makePrime(512)
            q = BigPrime.makePrime(513)
            rsa = RSA(p, q)
            rsa.setPublicKey(65537)
            print("p =", hex(p))
            print("q =", hex(q))
            print("Key Security Bits =", rsa.getSecurityBits())
            print("KEYpub:")
            print(rsa.getPublicKey())
            print("KEYprivate:")
            print(rsa.getPrivateKey())
            print("CipherText:")
            print(hex(rsa.Encryption(text)))
            return
    elif len(sys.argv) == 5:
        n = int(sys.argv[3], 16)
        key = int(sys.argv[4], 16)
        if deOrEn == '-e':
            print("Key Security Bits =", len(bin(n)) - 2)
            print("CipherText:")
            print(hex(RSA.EncryptionByKey(text, n, key)))
            return
        elif deOrEn == '-d':
            print("Key Security Bits =", len(bin(n)) - 2)
            print("CipherText:")
            print(hex(RSA.DecryptionByKey(text, n, key)))
            return
    elif len(sys.argv) == 6:
        p = int(sys.argv[3], 16)
        q = int(sys.argv[4], 16)
        key = int(sys.argv[5], 16)
        rsa = RSA(p, q)
        if deOrEn == '-e':
            rsa.setPublicKey(key)
            print("Key Security Bits =", rsa.getSecurityBits())
            print("CipherText:")
            print(hex(rsa.Encryption(text)))
            return
        elif deOrEn == '-d':
            rsa.setPrivateKey(key)
            print("Key Security Bits =", rsa.getSecurityBits())
            print("PlainText:")
            print(hex(rsa.Decryption(text)))
            return

    printHint()


if __name__ == "__main__":
    main()
