class RowTransposition:
    def Encryption(self, plaintext, key):
        encryptionList = ["" for i in range(len(key))]
        for index in range(len(plaintext)):
            encryptionList[int(key[index % len(key)]) - 1] += plaintext[index]
        encryption = ''.join(encryptionList)
        return encryption

    def Decryption(self, cipherText, key):
        decryptionList = ["" for i in range(len(key))]
        decryptionLen = [len(cipherText) // len(key) for i in range(len(key))]
        for index in range(len(cipherText) % len(key)):
            decryptionLen[int(key[index]) - 1] += 1
        decryptionIndex = 0
        for index in range(len(key)):
            decryptionList[index] = cipherText[decryptionIndex: decryptionIndex + decryptionLen[index]]
            decryptionIndex += decryptionLen[index]
        # print(decryptionList)
        decryption = ""
        for index in range(len(cipherText)):
            listIndex = int(key[index % len(key)]) - 1
            decryption += decryptionList[listIndex][0:1]
            decryptionList[listIndex] = decryptionList[listIndex][1:]
        return decryption
