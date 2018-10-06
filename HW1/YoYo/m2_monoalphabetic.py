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

    def Decryption(self, cipertext):
        # Make map
        monoMap = {}
        for i in range(26):
            monoMap[self.key[26 + i]] = self.key[i]

        # Decryption
        plaintext = ""
        for letter in cipertext.upper():
            transLetter = monoMap[letter]
            plaintext += transLetter

        return plaintext

def main():
    key = "zyxwvutsrqponmlkjihgfedcbaMNBVCXZLKJHGFDSAPOIUYTREWQ"
    method = Monoalphabetic(key)
    plaintext = 'keepgoingnevergiveup'
    cipertext = method.Encryption(plaintext)
    print(cipertext)
    print(method.Decryption(cipertext))

if __name__ == '__main__':
    main()
