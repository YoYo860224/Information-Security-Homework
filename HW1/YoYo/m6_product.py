class Product():
    def __init__(self, key, transport):
        self.key = key
        self.transport = transport

    def Encryption(self, plaintext):
        # Make Key Info
        keyList = self.key.split(' ')
        tranList = self.transport.split(' ')
        
        # Encryption
        ciphertextList = [''] * len(plaintext)
        for i in range(len(plaintext)):
            rounds = i // len(keyList)
            order = i % len(keyList)
            pos = tranList.index(keyList[order])
            ciphertextList[i] = plaintext[rounds * len(keyList) + pos]
        ciphertext = ''.join(ciphertextList)

        return ciphertext

    def Decryption(self, ciphertext):
        # Make Key Info
        keyList = self.key.split(' ')
        tranList = self.transport.split(' ')
        
        # Encryption
        plaintextList = [''] * len(ciphertext)
        for i in range(len(ciphertext)):
            rounds = i // len(keyList)
            order = i % len(keyList)
            pos = keyList.index(tranList[order])
            plaintextList[i] = ciphertext[rounds * len(keyList) + pos]
        plaintext = ''.join(plaintextList)

        return plaintext

def main(): 
    key = "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20"
    transport = "15 11 19 18 16 03 07 14 02 20 04 12 09 06 01 05 17 13 10 08"

    method = Product(key, transport)
    plaintext = 'keepgoingnevergiveup'
    cipertext = method.Encryption(plaintext)
    print(cipertext)
    print(method.Decryption(cipertext))

if __name__ == '__main__':
    main()
