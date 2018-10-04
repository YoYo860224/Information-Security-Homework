# Example :
# Plaintext = "keepgoingnevergiveup"
# key = 7


class Caesar():
    def Encryption(self):
        plaintext = input("Plese Enter the plaintext: ")
        key = int(input("Please Enter the key: "))
        encryption = ""
        for char in plaintext:
            ascNum = (ord(char.upper()) - ord('A') + key) % 26 + ord('A')
            encryption += chr(ascNum)
        print("encryption:", encryption)

    def Decryption(self):
        cipherText = input("Plese Enter the cipherText: ")
        key = int(input("Please Enter the key: "))
        decryption = ""
        for char in cipherText:
            ascNum = (ord(char.upper()) - ord('A') - key) % 26 + ord('A')
            decryption += chr(ascNum)
        print("decryption:", decryption)


cipher = Caesar()
cipher.Encryption()
print()
cipher.Decryption()
