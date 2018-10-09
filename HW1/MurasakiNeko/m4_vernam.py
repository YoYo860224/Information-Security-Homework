class Vernam:
    def Encryption(self, plaintext, key):
        plaintext = plaintext.upper()
        key = key.upper()
        encryptionKey = key + plaintext[:len(plaintext) - len(key)]
        encryption = ""
        for index in range(len(plaintext)):
            temp = (ord(plaintext[index]) - ord('A')) ^ (ord(encryptionKey[index]) - ord('A'))
            encryption += chr(temp + ord('A'))
        return encryption

    def Decryption(self, cipherText, key):
        key = key.upper()
        decryption = ""
        for index in range(len(cipherText)):
            temp = (ord(cipherText[index].upper()) - ord('A')) ^ (ord(key[index]) - ord('A'))
            decryption += chr(temp + ord('a'))
            key += chr(temp + ord('A'))
        return decryption
