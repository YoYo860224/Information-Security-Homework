input = "KeepGoingNeverGiveUp"
key = 7

print("input:", input, "key:", key)

# Encryption
encryption = ""
for char in input:
    if ord(char) >= ord('a'):
        base = ord('a')
    else:
        base = ord('A')
    encryption += chr((ord(char) - base + key) % 26 + base)
print("encryption:", encryption)
# Decryption
decryption = ""
for char in encryption:
    if ord(char) >= ord('a'):
        base = ord('a')
    else:
        base = ord('A')
    decryption += chr((ord(char) - base - key) % 26 + base)
print("decryption:", decryption)