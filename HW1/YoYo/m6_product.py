class Product():
    def __init__(self, key, transport):
        self.key = key
        self.transport = transport

    def Encryption(self, plaintext):
        # Make Key Info
        keyList = self.key.split(' ')
        tranList = self.transport.split(' ')

        # Encryption
        ciphertextList = [''] * len(keyList)
        for i in range(len(keyList)):
            pos = tranList.index(keyList[i])
            ciphertextList[pos] = plaintext[i]
        ciphertext = ''.join(ciphertextList)

        return ciphertext

    def Decryption(self, ciphertext):
        # Make Key Info
        keyList = self.key.split(' ')
        tranList = self.transport.split(' ')
        
        # Encryption
        plaintextList = [''] * len(keyList)
        for i in range(len(keyList)):
            pos = keyList.index(tranList[i])
            plaintextList[pos] = ciphertext[i]
        plaintext = ''.join(plaintextList)

        return plaintext

def main(): 
    key = "01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20"
    transport = "15 11 19 18 16 03 07 14 02 20 04 12 09 06 01 05 17 13 10 08"

    method = Product(key, transport)
    plaintext = 'keepgoingnevergiveup'
    ciphertext = method.Encryption(plaintext)
    print(ciphertext)
    print(method.Decryption(ciphertext))

if __name__ == '__main__':
    main()
