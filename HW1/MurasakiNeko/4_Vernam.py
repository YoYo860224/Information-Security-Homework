# Example :
# Plaintext = "keepgoingnevergiveup"
# key = "CON"


class Vernam:
    def Encryption(self):
        plaintext = input("Plese Enter the plaintext: ")
        key = input("Please Enter the key: ")
        encryptionKey = key.upper() + plaintext[:len(plaintext) - len(key)].upper()
        encryption = ""
        for index in range(len(plaintext)):
            temp = (ord(plaintext[index].upper()) - ord('A')) ^ (ord(encryptionKey[index]) - ord('A'))
            encryption += chr(temp + ord('A'))
        print("encryption:", encryption)

    def Decryption(self):
        cipherText = input("Plese Enter the cipherText: ")
        key = input("Please Enter the key: ")
        decryptionKey = key.upper()
        decryption = ""
        for index in range(len(cipherText)):
            temp = (ord(cipherText[index].upper()) - ord('A')) ^ (ord(decryptionKey[index]) - ord('A'))
            decryption += chr(temp + ord('A'))
            decryptionKey += chr(temp + ord('A'))
        print("decryption:", decryption)


cipher = Vernam()
cipher.Encryption()
print()
cipher.Decryption()
