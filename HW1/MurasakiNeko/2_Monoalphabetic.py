# Example :
# Plaintext = "keepgoingnevergiveup"
# key = "z:M, y:N, x:B, w:V, v:C, u:X, t:Z, s:L, r:K, q:J, p:H, o:G, n:F, m:D, l:S, k:A, j:P, i:O, h:I, g:U, f:Y, e:T, d:R, c:E, b:W, a:Q"


class Monoalphabetic:
    def Encryption(self):
        plaintext = input("Plese Enter the plaintext: ")
        key = input("Please Enter the key(format => z:M, y:N...): ")
        keyDict = {}
        for string in key.replace(' ', '').split(','):
            temp = string.split(':')
            keyDict.update({temp[0].upper(): temp[1].upper()})
        encryption = ""
        for char in plaintext.upper():
            encryption += keyDict[char]
        print("encryption:", encryption)

    def Decryption(self):
        cipherText = input("Plese Enter the cipherText: ")
        key = input("Please Enter the key(format => z:M, y:N...): ")
        keyDict = {}
        for string in key.replace(' ', '').split(','):
            temp = string.split(':')
            keyDict.update({temp[1].upper(): temp[0].upper()})
        decryption = ""
        for char in cipherText.upper():
            decryption += keyDict[char]
        print("decryption:", decryption)


cipher = Monoalphabetic()
cipher.Encryption()
print()
cipher.Decryption()
