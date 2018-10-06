class Vernam():
    def __init__(self, key):
        self.key = key

    def Encryption(self, plaintext):
        # Make autokey
        plaintext = plaintext.upper()
        autokey = (self.key + plaintext)[:len(plaintext)].upper()

        # Encryption
        ciphertext = ""
        for i in range(len(plaintext)):
            xorId = (ord(autokey[i]) - ord('A')) ^ (ord(plaintext[i]) - ord('A'))
            
            ciphertext += chr(ord('A') + xorId)

        return ciphertext

    def Decryption(self, ciphertext):
        # Make autokey
        ciphertext = ciphertext.upper()
        autokey = self.key.upper()

        # Decryption
        plaintext = ""
        for i in range(len(ciphertext)):
            xorId = (ord(autokey[i]) - ord('A')) ^ (ord(ciphertext[i]) - ord('A'))
            plaintext += chr(ord('A') + xorId)
            autokey += chr(ord('A') + xorId)
            
        return plaintext.lower()

def main(): 
    key = "CON" 
    method = Vernam(key)
    plaintext = 'keepgoingnevergiveup'
    ciphertext = method.Encryption(plaintext)
    print(ciphertext)
    print(method.Decryption(ciphertext))

if __name__ == '__main__':
    main()
