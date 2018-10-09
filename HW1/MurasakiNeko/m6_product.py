class Product:
    def Encryption(self, plaintext, key, transport):
        newPlaintext = ""
        for index in key.split(' '):
            newPlaintext += plaintext[int(index) - 1]
        encryption = ""
        for index in transport.split(' '):
            encryption += newPlaintext[int(index) - 1]
        return encryption

    def Decryption(self, cipherText, key, transport):
        transportList = [int(i) - 1 for i in transport.split(' ')]
        decryptionList = ['' for i in range(len(cipherText))]
        for index in range(len(cipherText)):
            decryptionList[transportList[index]] = cipherText[index]
        newCiphertext = ''.join(decryptionList)
        keyList = [int(i) - 1 for i in key.split(' ')]
        for index in range(len(newCiphertext)):
            decryptionList[keyList[index]] = newCiphertext[index]
        return ''.join(decryptionList)
