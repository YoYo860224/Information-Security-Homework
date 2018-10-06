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

    def Decryption(self, cipertext):
        # Make autokey
        cipertext = cipertext.upper()
        autokey = self.key.upper()

        # Decryption
        plaintext = ""
        for i in range(len(cipertext)):
            xorId = (ord(autokey[i]) - ord('A')) ^ (ord(cipertext[i]) - ord('A'))
            plaintext += chr(ord('A') + xorId)
            autokey += chr(ord('A') + xorId)
            
        return plaintext.lower()

def main(): 
    key = "CON" 
    method = Vernam(key)
    plaintext = 'keepgoingnevergiveup'
    cipertext = method.Encryption(plaintext)
    print(cipertext)
    print(method.Decryption(cipertext))

if __name__ == '__main__':
    main()
