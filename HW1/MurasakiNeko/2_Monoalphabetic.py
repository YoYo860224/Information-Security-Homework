input = "KeepGoingNeverGiveUp"
key = {'z':'M','y':'N','x':'B','w':'V','v':'C','u':'X','t':'Z','s':'L','r':'K','q':'J','p':'H','o':'G','n':'F' }
key.update({'m':'D','l':'S','k':'A','j':'P','i':'O','h':'I','g':'U','f':'Y','e':'T','d':'R','c':'E','b':'W','a':'Q'})

print("input:", input, "key:", key)

# Encryption
encryption = ""
for char in input:
    if ord(char) >= ord('a'):
        base = ord('a')
    else:
        base = ord('A')
    encryption += chr(ord(key[char.lower()]) - ord('A') + base)
print("encryption:", encryption)
# Decryption
inverseKey = {}
for elementKey, element in key.items():
    inverseKey[element] = elementKey
# print(inverseKey)

decryption = ""
for char in encryption:
    if ord(char) >= ord('a'):
        base = ord('a')
    else:
        base = ord('A')
    decryption += chr(ord(inverseKey[char.upper()]) - ord('a') + base)
print("decryption:", decryption)