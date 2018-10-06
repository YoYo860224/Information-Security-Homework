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

    def Decryption(self, cipertext):
        plaintext = ""
        for letter in cipertext.lower():
            shift = (ord(letter) - ord('a') - self.key) % 26
            transLetter = chr(ord('a') + shift)
            plaintext += transLetter
        return plaintext

def main(): 
    key = 7 
    method = Caesar(key)
    plaintext = 'keepgoingnevergiveup'
    cipertext = method.Encryption(plaintext)
    print(cipertext)
    print(method.Decryption(cipertext))

if __name__ == '__main__':
    main()
