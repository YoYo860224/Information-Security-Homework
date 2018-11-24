class DES:
    def __init__(self):
        self.__times = 1
        self.__lKey = []
        self.__rKey = []
        self.__IP = [58, 50, 42, 34, 26, 18, 10, 2,
                     60, 52, 44, 36, 28, 20, 12, 4,
                     62, 54, 46, 38, 30, 22, 14, 6,
                     64, 56, 48, 40, 32, 24, 16, 8,
                     57, 49, 41, 33, 25, 17, 9,  1,
                     59, 51, 43, 35, 27, 19, 11, 3,
                     61, 53, 45, 37, 29, 21, 13, 5,
                     63, 55, 47, 39, 31, 23, 15, 7]

        self.__IPInverse = [-1] * len(self.__IP)
        for index in range(len(self.__IP)):
            self.__IPInverse[self.__IP[index] - 1] = index + 1

        self.__E = [(start + index) % 32 + 1 for start in range(-1, 28, 4) for index in range(6)]

        self.__P = [16,  7, 20, 21, 29, 12, 28, 17,
                     1, 15, 23, 26,  5, 18, 31, 10,
                     2,  8, 24, 14, 32, 27,  3,  9,
                    19, 13, 30,  6, 22, 11,  4, 25]

        self.__PC1 = [57, 49, 41, 33, 25, 17,  9,
                       1, 58, 50, 42, 34, 26, 18,
                      10,  2, 59, 51, 43, 35, 27,
                      19, 11,  3, 60, 52, 44, 36,
                      63, 55, 47, 39, 31, 23, 15,
                       7, 62, 54, 46, 38, 30, 22,
                      14,  6, 61, 53, 45, 37, 29,
                      21, 13,  5, 28, 20, 12,  4]

        self.__PC2 = [14, 17, 11, 24,  1,  5,
                       3, 28, 15,  6, 21, 10,
                      23, 19, 12,  4, 26,  8,
                      16,  7, 27, 20, 13,  2,
                      41, 52, 31, 37, 47, 55,
                      30, 40, 51, 45, 33, 48,
                      44, 49, 39, 56, 34, 53,
                      46, 42, 50, 36, 29, 32]

        self.__S = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
                     0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
                     4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
                     15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],

                    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
                     3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
                     0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
                     13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],

                    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
                     13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
                     13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
                     1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],

                    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
                     13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
                     10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
                     3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],

                    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
                     14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
                     4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
                     11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],

                    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
                     10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
                     9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
                     4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],

                    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
                     13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
                     1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
                     6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],

                    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
                     1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
                     7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
                     2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

    @staticmethod
    def to64BitArray(bits):
        # 0xffffffffffffffff0000000000000000 -> ['11111111.....', '00000000..........']
        output = []
        bitsStr = ('0' * 63 + bin(bits)[2:])
        while(len(bitsStr) >= 64):
            output = [bitsStr[-64:]] + output
            bitsStr = bitsStr[:-64]
        return output

    @staticmethod
    def intToBitArray(bits):
        # '10110...' -> [1, 0, 1, 1, 0, ...]
        output = []
        for i in bits:
            output += [i]
        return [int(b) for b in bits]

    @staticmethod
    def bitArrayToInt(bitArray):
        # [1, 0, 1, 1, 0, ...] -> 10110...
        binStr = ''.join([str(b) for b in bitArray])
        return int(binStr, 2)

    def Encryption(self, plaintext, key):
        key = self.intToBitArray(self.to64BitArray(key)[0])
        # key 64 -> 56 by PC1
        key = self.__transport(key, self.__PC1)
        # C0 = lKey, D0 = rKey
        self.__lKey = key[:28]
        self.__rKey = key[28:]
        # Every 64 bit as a pair
        plaintexts = self.to64BitArray(plaintext)
        encryption = []
        for text in plaintexts:
            bits = self.intToBitArray(text)
            # Initial Permutation
            bits = self.__transport(bits, self.__IP)
            # Encryption 16 Round
            for times in range(16):
                self.__times = times + 1
                L = bits[:32]
                R = bits[32:]
                foutput = self.__fFunction(R, self.__getEnKey())
                bits = R + [L[index] ^ foutput[index] for index in range(32)]
            # Change at last time
            bits = bits[32:] + bits[:32]
            # Final Permutation
            bits = self.__transport(bits, self.__IPInverse)
            # ECB mode
            encryption += bits
        return self.bitArrayToInt(encryption)

    def Decryption(self, ciphertext, key):
        key = self.intToBitArray(self.to64BitArray(key)[0])
        # key 64 -> 56 by PC1
        key = self.__transport(key, self.__PC1)
        # C16 = lKey, D16 = rKey
        self.__lKey = key[:28]
        self.__rKey = key[28:]
        # Every 64 bit as a pair
        ciphertexts = self.to64BitArray(ciphertext)
        decryption = []
        for text in ciphertexts:
            bits = self.intToBitArray(text)
            # Initial Permutation
            bits = self.__transport(bits, self.__IP)
            # Change at last time
            bits = bits[32:] + bits[:32]
            for times in range(16):
                self.__times = 17 - times
                L = bits[:32]
                R = bits[32:]
                foutput = self.__fFunction(L, self.__getDeKey())
                bits = [R[index] ^ foutput[index] for index in range(32)] + L
            # Final Permutation
            bits = self.__transport(bits, self.__IPInverse)
            # ECB mode
            decryption += bits
            # Reset C16 D16
            self.__lKey = key[:28]
            self.__rKey = key[28:]
        return self.bitArrayToInt(decryption)

    def __transport(self, bits, vector):
        output = []
        for index in vector:
            output.append(bits[index - 1])
        return output

    def __fFunction(self, bits, key):
        # Expansion E
        bits = self.__transport(bits, self.__E)
        # XOR with round key
        bits = [bits[index] ^ key[index] for index in range(48)]
        # S-box substitution
        bits = self.__sBox(bits)
        # Permutation
        bits = self.__transport(bits, self.__P)
        return bits

    def __getEnKey(self):
        if self.__times in [1, 2, 9, 16]:
            # Rotated left by one bit
            self.__lKey = self.__lKey[1:] + self.__lKey[:1]
            self.__rKey = self.__rKey[1:] + self.__rKey[:1]
        else:
            # Rotated left by two bit
            self.__lKey = self.__lKey[2:] + self.__lKey[:2]
            self.__rKey = self.__rKey[2:] + self.__rKey[:2]
            # Selects a permuted subset of 48 bits
        return self.__transport(self.__lKey + self.__rKey, self.__PC2)

    def __getDeKey(self):
        if self.__times == 17:
            return self.__transport(self.__lKey + self.__rKey, self.__PC2)
        elif self.__times in [2, 9, 16]:
            # Rotated right by one bit
            self.__lKey = self.__lKey[-1:] + self.__lKey[:-1]
            self.__rKey = self.__rKey[-1:] + self.__rKey[:-1]
        else:
            # Rotated right by two bit
            self.__lKey = self.__lKey[-2:] + self.__lKey[:-2]
            self.__rKey = self.__rKey[-2:] + self.__rKey[:-2]
            # Selects a permuted subset of 48 bits
        return self.__transport(self.__lKey + self.__rKey, self.__PC2)

    def __sBox(self, bits):
        output = []
        for start in range(0, 48, 6):
            row = bits[start] * 2 + bits[5 + start]
            col = bits[start + 1] * 8 + bits[start + 2] * 4 + bits[start + 3] * 2 + bits[start + 4]
            output += [int(bit) for bit in ('000000' + bin(self.__S[start // 6][row * 16 + col])[2:])[-4:]]
        return output
