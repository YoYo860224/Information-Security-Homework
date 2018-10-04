# input = "keepgoingnevergiveup"
# key = "31562487"
input = "attackpostponeduntiltwoamxyz"
key = "4312567"

print("input:", input, "key:", key)

# Encryption
encryptionList = ["" for i in range(len(key))]
for index in range(len(input)):
    encryptionList[int(key[index % len(key)]) - 1] += input[index]
encryption = ''.join(encryptionList)
# print(encryptionList)
print("encryption:", encryption)
# Decryption
decryptionList = ["" for i in range(len(key))]
decryptionLen = [len(encryption) // len(key) for i in range(len(key))]
for index in range(len(encryption) % len(key)):
    decryptionLen[int(key[index]) - 1] += 1
decryptionIndex = 0
for index in range(len(key)):
    decryptionList[index] = encryption[decryptionIndex:decryptionIndex + decryptionLen[index]]
    decryptionIndex += decryptionLen[index]
# print(decryptionList)
decryption = ""
for index in range(len(input)):
    listIndex = int(key[index % len(key)]) - 1
    decryption += decryptionList[listIndex][0:1]
    decryptionList[listIndex] = decryptionList[listIndex][1:]
print("decryption:", decryption)
