class Playfair():
    def __init__(self, key):
        self.key = key

    def Encryption(self, plaintext):
        # Make table as string
        pfTable = ""
        for i in range(26):
            pfTable += chr(ord('A') + i)
        for letter in self.key.upper():
            pfTable = pfTable.replace(letter, "")
        pfTable = self.key + pfTable
        pfTable = pfTable.replace('J', "")

        # Porcess plaintext
        plainGroup = []
        plaintext = plaintext.upper().replace("J", "I")
        while plaintext != "":
            # Last one
            if len(plaintext) == 1:
                thisGroup = plaintext + "X"
                plainGroup.append(thisGroup)
                plaintext = ""
            # Repeat
            elif plaintext[0] == plaintext[1]:
                thisGroup = plaintext[0] + "X"
                plainGroup.append(thisGroup)
                plaintext = plaintext[1:]
            # Others
            else:
                thisGroup = plaintext[:2]
                plainGroup.append(thisGroup)
                plaintext = plaintext[2:]
        
        # Encryption
        ciphertext = ""
        for i in plainGroup:
            row0 = pfTable.find(i[0]) // 5
            col0 = pfTable.find(i[0]) %  5
            row1 = pfTable.find(i[1]) // 5
            col1 = pfTable.find(i[1]) %  5
            if row0 == row1:
                ciphertext += pfTable[row0 * 5 + (col0 + 1) % 5]
                ciphertext += pfTable[row1 * 5 + (col1 + 1) % 5]
            elif col0 == col1:
                ciphertext += pfTable[(row0 + 1) % 5 * 5 + col0]
                ciphertext += pfTable[(row1 + 1) % 5 * 5 + col1]
            else:
                ciphertext += pfTable[row0 * 5 + col1]
                ciphertext += pfTable[row1 * 5 + col0]
       
        return ciphertext

    def Decryption(self, ciphertext):
        # Make table as string
        pfTable = ""
        for i in range(26):
            pfTable += chr(ord('A') + i)
        for letter in self.key.upper():
            pfTable = pfTable.replace(letter, "")
        pfTable = self.key + pfTable
        pfTable = pfTable.replace('J', "")

        # Porcess plaintext
        plainGroup = []
        while ciphertext != "":
            thisGroup = ciphertext[:2]
            plainGroup.append(thisGroup)
            ciphertext = ciphertext[2:]

        # Decryption
        ciphertext = ""
        for i in plainGroup:
            row0 = pfTable.find(i[0]) // 5
            col0 = pfTable.find(i[0]) %  5
            row1 = pfTable.find(i[1]) // 5
            col1 = pfTable.find(i[1]) %  5
            if row0 == row1:
                ciphertext += pfTable[row0 * 5 + (col0 - 1) % 5]
                ciphertext += pfTable[row1 * 5 + (col1 - 1) % 5]
            elif col0 == col1:
                ciphertext += pfTable[(row0 - 1) % 5 * 5 + col0]
                ciphertext += pfTable[(row1 - 1) % 5 * 5 + col1]
            else:
                ciphertext += pfTable[row0 * 5 + col1]
                ciphertext += pfTable[row1 * 5 + col0]
       
        return ciphertext.lower()

def main():
    key = "HIT"
    method = Playfair(key)
    plaintext = 'keepgoingnevergiveup'
                 
    ciphertext = method.Encryption(plaintext)
    print(ciphertext)
    print(method.Decryption(ciphertext))

if __name__ == '__main__':
    main()
