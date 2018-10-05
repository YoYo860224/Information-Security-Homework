# Example :
# Plaintext = "keepgoingnevergiveup"
# key = "HIT"


class Playfair:
    def Encryption(self):
        plaintext = input("Plese Enter the plaintext: ")
        key = input("Please Enter the key: ").upper()
        # Process key to playfair key table
        playfairKey = {}
        index = 0
        for char in (key + ''.join([chr(i + ord('A')) for i in range(26)])).replace('J', 'I'):
            if char not in playfairKey.keys():
                playfairKey[char] = [index // 5, index % 5]
                index += 1
        playfairKey['J'] = playfairKey['I']
        playfairKeyInverse = [i for i in range(25)]
        for char, val in playfairKey.items():
            if char != 'J':
                playfairKeyInverse[val[0] * 5 + val[1]] = char
        # Add X to plaintext when two letter is same
        newPlaintext = ""
        for char in plaintext.upper():
            if newPlaintext[:1] == char:
                newPlaintext += 'X'
            newPlaintext += char
        if len(newPlaintext) % 2 != 0:
            newPlaintext += 'X'
        # Encryption
        encryption = ""
        for index in range(0, len(newPlaintext), 2):
            first = playfairKey[newPlaintext[index]]
            second = playfairKey[newPlaintext[index + 1]]
            if first[0] != second[0] and first[1] != second[1]:
                encryption += playfairKeyInverse[first[0] * 5 + second[1]]
                encryption += playfairKeyInverse[second[0] * 5 + first[1]]
            elif first[1] == second[1]:
                encryption += playfairKeyInverse[(first[0] + 1) % 5 * 5 + first[1]]
                encryption += playfairKeyInverse[(second[0] + 1) % 5 * 5 + second[1]]
            else:
                encryption += playfairKeyInverse[first[0] * 5 + (first[1] + 1) % 5]
                encryption += playfairKeyInverse[second[0] * 5 + (second[1] + 1) % 5]
        print("encryption:", encryption)

    def Decryption(self):
        cipherText = input("Plese Enter the cipherText: ")
        key = input("Please Enter the key: ").upper()
        # Process key to playfair key table
        playfairKey = {}
        index = 0
        for char in (key.join([chr(i + ord('A')) for i in range(26)])).replace('J', 'I'):
            if char not in playfairKey.keys():
                playfairKey[char] = [index // 5, index % 5]
                index += 1
        playfairKey['J'] = playfairKey['I']
        playfairKeyInverse = [i for i in range(25)]
        for char, val in playfairKey.items():
            if char != 'J':
                playfairKeyInverse[val[0] * 5 + val[1]] = char
        # Decryption
        decryption = ""
        for index in range(0, len(cipherText), 2):
            first = playfairKey[cipherText[index]]
            second = playfairKey[cipherText[index + 1]]
            if first[0] != second[0] and first[1] != second[1]:
                decryption += playfairKeyInverse[first[0] * 5 + second[1]]
                decryption += playfairKeyInverse[second[0] * 5 + first[1]]
            elif first[1] == second[1]:
                decryption += playfairKeyInverse[(first[0] + 4) % 5 * 5 + first[1]]
                decryption += playfairKeyInverse[(second[0] + 4) % 5 * 5 + second[1]]
            else:
                decryption += playfairKeyInverse[first[0] * 5 + (first[1] + 4) % 5]
                decryption += playfairKeyInverse[second[0] * 5 + (second[1] + 4) % 5]
        print("decryption:", decryption)


cipher = Playfair()
cipher.Encryption()
print()
cipher.Decryption()
