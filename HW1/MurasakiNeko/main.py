import sys
from m1_caesar import Caesar
from m2_monoalphabetic import Monoalphabetic
from m3_playfair import Playfair
from m4_vernam import Vernam
from m5_row_transposition import RowTransposition
from m6_product import Product


def main():
    if len(sys.argv) < 4:
        print('Usage: -e <plaintext> <method>')
        print('Usage: -d <ciphertext> <method>')
        print('<method>:')
        print('\t1.Caesar')
        print('\t2.Monoalphabetic')
        print('\t3.Playfair')
        print('\t4.Vernam')
        print('\t5.RowTransposition')
        print('\t6.Product')
        return

    deOrEn = sys.argv[1]
    text = sys.argv[2]
    inputMethod = sys.argv[3]

    if deOrEn == '-e':
        if inputMethod == "1":
            key = input("input key (ex. '7'):\n")
            print(Caesar().Encryption(text, key))
        elif inputMethod == "2":
            key = input("input key (ex. 'zyxwvutsrqponmlkjihgfedcbaMNBVCXZLKJHGFDSAPOIUYTREWQ'):\n")
            print(Monoalphabetic().Encryption(text, key))
        elif inputMethod == "3":
            key = input("input key (ex. 'HIT'):\n")
            print(Playfair().Encryption(text, key))
        elif inputMethod == "4":
            key = input("input key (ex. 'CON'):\n")
            print(Vernam().Encryption(text, key))
        elif inputMethod == "5":
            key = input("input key (ex. '31562487'):\n")
            print(RowTransposition().Encryption(text, key))
        elif inputMethod == "6":
            key = input("input key (ex. '01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20'):\n")
            transport = input("Input transport (ex. '15 11 19 18 16 03 07 14 02 20 04 12 09 06 01 05 17 13 10 08'):\n")
            print(Product().Encryption(text, key, transport))
    elif deOrEn.lower() == '-d':
        if inputMethod == "1":
            key = input("input key (ex. '7'):\n")
            print(Caesar().Decryption(text, key))
        elif inputMethod == "2":
            key = input("input key (ex. 'zyxwvutsrqponmlkjihgfedcbaMNBVCXZLKJHGFDSAPOIUYTREWQ'):\n")
            print(Monoalphabetic().Decryption(text, key))
        elif inputMethod == "3":
            key = input("input key (ex. 'HIT'):\n")
            print(Playfair().Decryption(text, key))
        elif inputMethod == "4":
            key = input("input key (ex. 'CON'):\n")
            print(Vernam().Decryption(text, key))
        elif inputMethod == "5":
            key = input("input key (ex. '31562487'):\n")
            print(RowTransposition().Decryption(text, key))
        elif inputMethod == "6":
            key = input("input key (ex. '01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20'):\n")
            transport = input("Input transport (ex. '15 11 19 18 16 03 07 14 02 20 04 12 09 06 01 05 17 13 10 08'):\n")
            print(Product().Decryption(text, key, transport))


if __name__ == '__main__':
    main()
