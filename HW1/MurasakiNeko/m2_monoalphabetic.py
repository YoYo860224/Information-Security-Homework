class Monoalphabetic:
    def Encryption(self, plaintext, key):
        key = key.upper()
        keyDict = {}
        for index in range(26):
            keyDict[key[index]] = key[index + 26]
        encryption = ""
        for char in plaintext.upper():
            encryption += keyDict[char]
        return encryption

    def Decryption(self, cipherText, key):
        key = key.upper()
        keyDict = {}
        for index in range(26):
            keyDict[key[index + 26]] = key[index]
        decryption = ""
        for char in cipherText.upper():
            decryption += keyDict[char]
        return decryption.lower()
