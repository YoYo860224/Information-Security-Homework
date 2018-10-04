# plaintext = "keepgoingnevergiveup"
# key = [15, 11, 19, 18, 16, 3, 7, 14, 2, 20, 4, 12, 9, 6, 1, 5, 17, 13, 10, 8]
# CipherText

plaintext = "thestrengthofthispig"
key = [15, 11, 19, 18, 16, 3, 7, 14, 2, 20, 4, 12, 9, 6, 1, 5, 17, 13, 10, 8]

# Encryption
encryption = ""
for index in range(len(plaintext)):
    encryption += plaintext[key[index % len(key)] - 1].upper()
print("encryption:", encryption)
# Decryption
decryptionList = ['' for i in range(len(encryption))]
for index in range(len(encryption)):
    decryptionList[key[index % len(key)] - 1] = encryption[index]
print("decryption:", ''.join(decryptionList))
