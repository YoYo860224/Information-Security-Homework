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
    if index + 1 == len(input) or input[index] == input[index + 1]:
        newInput.append(input[index] + 'X')
        index += 1
    else:
        newInput.append(input[index] + input[index + 1])
        index += 2
print(newInput)
# Decryption
