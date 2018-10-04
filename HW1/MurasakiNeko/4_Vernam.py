input = "keepgoingnevergiveup"
key = "CON"
# input = "helo"
# key = "qijf"

print("input:", input, "key:", key)

# Encryption
encryptionKey = key.upper() + input[:len(input) - len(key)].upper()
encryption = ""
for index in range(len(input)):
    temp = (ord(input[index].upper()) - ord('A')) ^ (ord(encryptionKey[index]) - ord('A'))
    encryption += chr(temp + ord('A'))
print("encryption:", encryption)
# Decryption
decryptionKey = key.upper()
decryption = ""
for index in range(len(encryption)):
    temp = (ord(encryption[index].upper()) - ord('A')) ^ (ord(decryptionKey[index]) - ord('A'))
    decryption += chr(temp + ord('A'))
    decryptionKey += chr(temp + ord('A'))
print("decryption:", decryption)
