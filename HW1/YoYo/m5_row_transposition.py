class RowTransposition():
    def __init__(self, key):
        self.key = key

    def Encryption(self, plaintext):
        ciphertextList = [""] * len(self.key)
        for i, letter in enumerate(plaintext):
            cCol = i % len(self.key)
            keyOrder = int(self.key[cCol]) - 1
            ciphertextList[keyOrder] += letter
        ciphertext = ''.join(ciphertextList)

        return ciphertext

    def Decryption(self, ciphertext):
        keyLen = len(self.key)
        cipherLen = len(ciphertext)

        plaintextList = [""] * keyLen
        for i in range(keyLen):
            length = cipherLen // keyLen
            order = self.key.find(str(i + 1))
            if order < (cipherLen % keyLen):
                length += 1
            plaintextList[order] = ciphertext[:length]
            ciphertext = ciphertext[length:]

        plaintext = ""
        for i in range(cipherLen):
            plaintext += plaintextList[i % keyLen][i // keyLen]

        return plaintext

def main(): 
    key = "31562487"
    
    method = RowTransposition(key)
    plaintext = 'keepgoingnevergiveup'
    cipertext = method.Encryption(plaintext)
    print(cipertext)
    print(method.Decryption(cipertext))

if __name__ == '__main__':
    main()
