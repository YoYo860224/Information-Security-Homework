input = "keepgoingnevergiveup"
key = "CON"

print("input:", input, "key:", key)

# Encryption
encryption = ""
index = 0
for char in input:
    encryption += chr((ord(char.upper()) +
                       ord(key[index].upper()) - 2 * ord('A')) % 26 + ord('A'))
    index = (index + 1) % len(key)
print("encryption:", encryption)
# Decryption
decryption = ""
index = 0
for char in encryption:
    decryption += chr((ord(char.upper()) -
                       ord(key[index].upper()) - 2 * ord('A') + 26) % 26 + ord('A'))
    index = (index + 1) % len(key)
print("decryption:", decryption)
