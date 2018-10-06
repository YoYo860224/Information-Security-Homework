import sys
from m1_caesar import Caesar
from m2_monoalphabetic import Monoalphabetic
from m3_playfair import Playfair
from m4_vernam import Vernam
from m5_row_transposition import RowTransposition
from m6_product import Product

def main():
    if len(sys.argv) < 4:
        print('Usage: ./main.py -e <method> <plaintext>')
        print('Usage: ./main.py -d <method> <ciphertext>')
        print('<method>:')
        print('\t1.Caesar')
        print('\t2.Monoalphabetic')
        print('\t3.Playfair')
        print('\t4.Vernam')
        print('\t5.RowTransposition')
        print('\t6.Product')
        return

    deOrEn = sys.argv[1]
    inputMethod = sys.argv[2]
    text = sys.argv[3]
    
    if deOrEn == '-e':
        if inputMethod == "1":
            key = input("input key (ex. '1'):")
            print(Caesar(int(key)).Encryption(text))
        elif inputMethod == "2":
            key = input("input key (ex. 'zyxwvutsrqponmlkjihgfedcbaMNBVCXZLKJHGFDSAPOIUYTREWQ'):")
            print(Monoalphabetic(key).Encryption(text))
        elif inputMethod == "3":
            key = input("input key (ex. 'HIT'):")
            print(Playfair(key).Encryption(text))
        elif inputMethod == "4":
            key = input("input key (ex. 'CON'):")
            print(Vernam(key).Encryption(text))
        elif inputMethod == "5":
            key = input("input key (ex. '31562487'):")
            print(RowTransposition(key).Encryption(text))
        elif inputMethod == "6":
            key = input("Input key (ex. '1 2 3'):\n")
            transport = input("Input transport (ex. '3 2 1'):\n")
            print(Product(key, transport).Encryption(text))
    elif deOrEn.lower() == '-d':
        if inputMethod == "1":
            key = input("input key (ex. '1'):")
            print(Caesar(int(key)).Decryption(text))
        elif inputMethod == "2":
            key = input("input key (ex. 'zyxwvutsrqponmlkjihgfedcbaMNBVCXZLKJHGFDSAPOIUYTREWQ'):")
            print(Monoalphabetic(key).Decryption(text))
        elif inputMethod == "3":
            key = input("input key (ex. 'HIT'):")
            print(Playfair(key).Decryption(text))
        elif inputMethod == "4":
            key = input("input key (ex. 'CON'):")
            print(Vernam(key).Decryption(text))
        elif inputMethod == "5":
            key = input("input key (ex. '31562487'):")
            print(RowTransposition(key).Decryption(text))
        elif inputMethod == "6":
            key = input("Input key (ex. '1 2 3'):\n")
            transport = input("Input transport (ex. '3 2 1'):\n")
            print(Product(key, transport).Decryption(text))

if __name__ == '__main__':
    main()