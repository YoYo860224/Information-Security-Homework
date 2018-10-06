class Caesar():
    def __init__(self, key):
        self.key = key

    def Encryption(self, plaintext):
        ciphertext = ""
        for letter in plaintext.upper():
            shift = (ord(letter) - ord('A') + self.key) % 26
            transLetter = chr(ord('A') + shift)
            ciphertext += transLetter

        return ciphertext

    def Decryption(self, ciphertext):
        plaintext = ""
        for letter in ciphertext.lower():
            shift = (ord(letter) - ord('a') - self.key) % 26
            transLetter = chr(ord('a') + shift)
            plaintext += transLetter
            
        return plaintext

def main(): 
    key = 7 
    method = Caesar(key)
    plaintext = 'keepgoingnevergiveup'
    ciphertext = method.Encryption(plaintext)
    print(ciphertext)
    print(method.Decryption(ciphertext))

if __name__ == '__main__':
    main()
