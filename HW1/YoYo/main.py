from m1_caesar import Caesar
from m2_monoalphabetic import Monoalphabetic
from m3_playfair import Playfair

def main():
    print('1.Caesar')
    print('2.Monoalphabetic')
    print('3.Playfair')

    inputMethod = input('Choice Method:')
    inputKey = input('Input key:')
    deOrEn = str(input('Encryption or Decryption(\'e\'or\'d\'):'))
    if deOrEn.lower() == 'e':
        plaintext = input('Input plaintext:')

        if inputMethod == "1":
            method = Caesar(inputKey)
            print("ciphertext is ", method.Encryption(plaintext))
        elif inputMethod == "2":
            method = Monoalphabetic(inputKey)
            print("ciphertext is ", method.Encryption(plaintext))
        elif inputMethod == "3":
            method = Playfair(inputKey)
            print("ciphertext is ", method.Encryption(plaintext))
    elif deOrEn.lower() == 'd':
        ciphertext = input('Input ciphertext:')

        if inputMethod == "1":
            method = Caesar(inputKey)
            print("ciphertext is ", method.Decryption(ciphertext))
        elif inputMethod == "2":
            method = Monoalphabetic(inputKey)
            print("ciphertext is ", method.Decryption(ciphertext))
        elif inputMethod == "3":
            method = Playfair(inputKey)
            print("ciphertext is ", method.Decryption(ciphertext))
        else:
            print("input ERROR")


if __name__ == '__main__':
    main()