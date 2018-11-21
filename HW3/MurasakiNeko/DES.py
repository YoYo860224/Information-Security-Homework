class DES:
    def __init__(self):
        self.IP = [58, 50, 42, 34, 26, 18, 10, 2,
                   60, 52, 44, 36, 28, 20, 12, 4,
                   62, 54, 46, 38, 30, 22, 14, 6,
                   64, 56, 48, 40, 32, 24, 16, 8,
                   57, 49, 41, 33, 25, 17, 9, 1,
                   59, 51, 43, 35, 27, 19, 11, 3,
                   61, 53, 45, 37, 29, 21, 13, 5,
                   63, 55, 47, 39, 31, 23, 15, 7]
        # for index in range(0, len(self.IP), 8):
        #     print(self.IP[index:index + 8])

        self.IPInverse = [-1] * len(self.IP)
        for index in range(len(self.IP)):
            self.IPInverse[self.IP[index] - 1] = index + 1
        # for index in range(0, len(self.IPInverse), 8):
        #     print(self.IPInverse[index:index + 8])

        self.E = [(start + index) % 32 + 1 for start in range(-1, 28, 4) for index in range(6)]
        # for index in range(0, len(self.E), 6):
        #     print(self.E[index:index + 6])

        self.PC1 = [57, 49, 41, 33, 25, 17, 9,
                    1, 58, 50, 42, 34, 26, 18,
                    10, 2, 59, 51, 43, 35, 27,
                    19, 11, 3, 60, 52, 44, 36,
                    63, 55, 47, 39, 31, 23, 15,
                    7, 62, 54, 46, 38, 30, 22,
                    14, 6, 61, 53, 45, 37, 29,
                    21, 13, 5, 28, 20, 12, 4]

        self.PC2 = [14, 17, 11, 24, 1, 5,
                    3, 28, 15, 6, 21, 10,
                    23, 19, 12, 4, 26, 8,
                    16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32]

    @staticmethod
    def toBits(string):
        output = []
        for char in string:
            bits = bin(ord(char))[2:]
            bits = '00000000'[len(bits):] + bits
            output.extend([int(b) for b in bits])
        return output

    @staticmethod
    def toStr(bits):
        string = []
        for b in range(len(bits) // 8):
            byte = bits[b * 8:(b + 1) * 8]
            string.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(string)

    def Encryption(self, plaintext, key):
        key = self.toBits(key)
        key = [key[index] for index in range(len(key)) if index % 8 != 7]
        plaintext = [(plaintext[index:index + 8] + chr(0) * 7)[:8] for index in range(0, len(plaintext), 8)]
        print(plaintext)
        encryption = ""
        return encryption


des = DES()
des.Encryption("apple123456", "apple123")
