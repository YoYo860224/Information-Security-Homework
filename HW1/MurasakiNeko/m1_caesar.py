class Caesar():
    def Encryption(self, plaintext, key):
        key = int(key)
        encryption = ""
        for char in plaintext.upper():
            encryption += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        return encryption

    def Decryption(self, cipherText, key):
        key = int(key)
        decryption = ""
        for char in cipherText.upper():
            decryption += chr((ord(char) - ord('A') - key) % 26 + ord('a'))
        return decryption
