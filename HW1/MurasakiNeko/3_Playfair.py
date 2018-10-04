input = "keepgoingnevergiveup"
key = "HIT"
print("input:", input, "key:", key)

# Encryption
# J = I
key = key.upper().replace('J', 'I')
newKey = ""
for char in key:
    if char not in newKey:
        newKey += char

# print(newKey)
temp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
playfairKey = {x: -1 for x in temp}
temp = temp.replace('J', '')
index = 0
for char in newKey:
    playfairKey[char.upper()] = index
    temp = temp.replace(char, '')
    index += 1
for char in temp:
    playfairKey[char] = index
    index += 1
playfairKey['J'] = playfairKey['I']
playfairKeyInverse = [i for i in range(25)]
for k, v in playfairKey.items():
    if k != 'J':
        playfairKeyInverse[v] = k
# print(playfairKey)
# for i in range(5):
#     for j in range(5):
#         for k, v in playfairKey.items():
#             if v == i * 5 + j:
#                 print(k, end=', ')
#                 break
#     print()

newInput = []
index = 0
while index < len(input):
    if index + 1 == len(input) or input[index].upper() == input[index + 1].upper():
        newInput.append(input[index].upper() + 'X')
        index += 1
    else:
        newInput.append(input[index].upper() + input[index + 1].upper())
        index += 2
# print(newInput)
encryption = ""
for string in newInput:
    first = [playfairKey[string[0]] // 5, playfairKey[string[0]] % 5]
    second = [playfairKey[string[1]] // 5, playfairKey[string[1]] % 5]
    if first[0] != second[0] and first[1] != second[1]:
        encryption += playfairKeyInverse[first[0] * 5 + second[1]]
        encryption += playfairKeyInverse[second[0] * 5 + first[1]]
    elif first[1] == second[1]:
        encryption += playfairKeyInverse[(first[0] + 1) % 5 * 5 + first[1]]
        encryption += playfairKeyInverse[(second[0] + 1) % 5 * 5 + second[1]]
    else:
        encryption += playfairKeyInverse[first[0] * 5 + (first[1] + 1) % 5]
        encryption += playfairKeyInverse[second[0] * 5 + (second[1] + 1) % 5]
print(encryption)
# Decryption
decryption = ""
for index in range(0, len(encryption), 2):
    first = [playfairKey[encryption[index]] // 5]
    first.append(playfairKey[encryption[index]] % 5)
    second = [playfairKey[encryption[index + 1]] // 5]
    second.append(playfairKey[encryption[index + 1]] % 5)
    if first[0] != second[0] and first[1] != second[1]:
        decryption += playfairKeyInverse[first[0] * 5 + second[1]]
        decryption += playfairKeyInverse[second[0] * 5 + first[1]]
    elif first[1] == second[1]:
        decryption += playfairKeyInverse[(first[0] + 4) % 5 * 5 + first[1]]
        decryption += playfairKeyInverse[(second[0] + 4) % 5 * 5 + second[1]]
    else:
        decryption += playfairKeyInverse[first[0] * 5 + (first[1] + 4) % 5]
        decryption += playfairKeyInverse[second[0] * 5 + (second[1] + 4) % 5]
print(decryption)

# Question:
# How to know it is I or J?
# How to remove X?
