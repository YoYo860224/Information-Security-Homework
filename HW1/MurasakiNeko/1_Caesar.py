input = "keepgoingnevergiveup"
key = 7

print("input:", input, "key:", key)

# Encryption
encryption = ""
for char in input:
    encryption += chr((ord(char.upper()) - ord('A') + key) % 26 + ord('A'))
print("encryption:", encryption)
# Decryption
decryption = ""
for char in encryption:
    decryption += chr((ord(char.upper()) - ord('A') - key) % 26 + ord('A'))
print("decryption:", decryption)
