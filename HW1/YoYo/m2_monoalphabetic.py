class Monoalphabetic():
    def __init__(self, key):
        self.key = key

    def Encryption(self, plaintext):       
        # Make map
        monoMap = {}
        for i in range(26):
            monoMap[self.key[i]] = self.key[26 + i]

        # Encryption
        ciphertext = ""
        for letter in plaintext.lower():
            transLetter = monoMap[letter]
            ciphertext += transLetter
            
        return ciphertext

    def Decryption(self, ciphertext):
        # Make map
        monoMap = {}
        for i in range(26):
            monoMap[self.key[26 + i]] = self.key[i]

        # Decryption
        plaintext = ""
        for letter in ciphertext.upper():
            transLetter = monoMap[letter]
            plaintext += transLetter

        return plaintext

def main():
    key = "zyxwvutsrqponmlkjihgfedcbaMNBVCXZLKJHGFDSAPOIUYTREWQ"
    method = Monoalphabetic(key)
    plaintext = 'keepgoingnevergiveup'
    ciphertext = method.Encryption(plaintext)
    print(ciphertext)
    print(method.Decryption(ciphertext))

if __name__ == '__main__':
    main()
