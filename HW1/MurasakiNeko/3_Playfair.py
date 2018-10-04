input = "kkeepgoingnevergiveup"
key = "HIT"
print("input:", input, "key:", key)

# Encryption
# I = J
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
    firstIndex = [playfairKey[string[0]] // 5, playfairKey[string[0]] % 5]
    secondIndex = [playfairKey[string[1]] // 5, playfairKey[string[1]] % 5]
    if firstIndex[0] != secondIndex[0] and firstIndex[1] != secondIndex[1]:
        encryption += playfairKeyInverse[firstIndex[0] * 5 + secondIndex[1]] + playfairKeyInverse[firstIndex[1] * 5 + secondIndex[0]]
    elif firstIndex[1] == secondIndex[1]:
        encryption += playfairKeyInverse[(firstIndex[0] + 1) % 5 * 5 + firstIndex[1]] + playfairKeyInverse[(secondIndex[1] + 1) % 5 * 5 + firstIndex[0]]
    else:
        encryption += playfairKeyInverse[firstIndex[0] * 5 + (firstIndex[1] + 1) % 5] + playfairKeyInverse[firstIndex[0] * 5 + (secondIndex[1] + 1) % 5]
print(encryption)
# Decryption
