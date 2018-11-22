import sys
from DES import DES

def main():
    if len(sys.argv) < 4:
        print('Usage: -e <plaintext> <key>')
        print('Usage: -d <ciphertext> <key>')
        return

    des = DES()

    deOrEn = sys.argv[1]
    text = int(sys.argv[2], 16)
    key = int(sys.argv[3], 16)

    if deOrEn == '-e':
        cipherT = des.Encryption(text, key)
        print(hex(cipherT))
    elif deOrEn.lower() == '-d':
        plainT = des.Decryption(text, key)
        print(hex(plainT))

if __name__ == "__main__":
    main()