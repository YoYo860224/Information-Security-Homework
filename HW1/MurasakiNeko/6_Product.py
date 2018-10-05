# Example :
# Plaintext = "keepgoingnevergiveup"
# Key = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
# Transport = "15 11 19 18 16 3 7 14 2 20 4 12 9 6 1 5 17 13 10 8"


class Product:
    def Encryption(self):
        plaintext = input("Plese Enter the plaintext: ")
        key = input("Please Enter the key: ")
        transport = input("Please Enter the transport: ")
        newPlaintext = ""
        for index in key.split(' '):
            newPlaintext += plaintext[int(index) - 1]
        encryption = ""
        for index in transport.split(' '):
            encryption += newPlaintext[int(index) - 1].upper()
        print("encryption:", encryption)

    def Decryption(self):
        cipherText = input("Plese Enter the cipherText: ")
        key = input("Please Enter the key: ")
        transport = input("Please Enter the transport: ")
        transportList = [int(i) - 1 for i in transport.split(' ')]
        decryptionList = ['' for i in range(len(cipherText))]
        for index in range(len(cipherText)):
            decryptionList[transportList[index]] = cipherText[index]
        newCiphertext = ''.join(decryptionList)
        keyList = [int(i) - 1 for i in key.split(' ')]
        for index in range(len(newCiphertext)):
            decryptionList[keyList[index]] = newCiphertext[index]
        print("decryption:", ''.join(decryptionList))


cipher = Product()
cipher.Encryption()
print()
cipher.Decryption()
