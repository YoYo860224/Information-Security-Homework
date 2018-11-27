class RSA:
    def __init__(self, p, q):
        # init RSA
        self.p = p
        self.q = q
        self.n = p * q
        # pick a public key
        self.e = 3 if self.n < 10000 else 17
        self.phi_n = (self.p - 1) * (self.q - 1)
        # compute private key
        self.d = self.__ModularInverse(self.e, self.phi_n)
        # precompute for decryption (using Chinese Remainder Theorem)
        self.Dp = self.d % (self.p - 1)
        self.Dq = self.d % (self.q - 1)
        self.t = self.__ModularInverse(self.p, self.q)

    def __ExtendGCD(self, a, b):
        if b == 0:
            return 1, 0
        else:
            x, y = self.__ExtendGCD(b, a % b)
            return y, (x - (a // b) * y)

    def __ModularInverse(self, val, mod):
        return self.__ExtendGCD(val, mod)[0] % mod

    def setPublicKey(self, e):
        self.e = e
        self.d = self.__ModularInverse(self.e, self.phi_n)
        self.Dp = self.d % (self.p - 1)
        self.Dq = self.d % (self.q - 1)

    def setPrivateKey(self, d):
        self.d = d
        self.e = self.__ModularInverse(self.d, self.phi_n)
        self.Dp = self.d % (self.p - 1)
        self.Dq = self.d % (self.q - 1)

    def getPublicKey(self):
        return hex(self.n), hex(self.e)

    def getPrivateKey(self):
        return hex(self.n), hex(self.d)

    def getSecurityBits(self):
        return len(bin(self.n)) - 2

    @staticmethod
    def __pow(x, y, z):
        # Square & multiply
        output = 1
        for bit in bin(y)[2:]:
            output *= output
            if bit == "1":
                output *= x
            output %= z
        return output

    @staticmethod
    def EncryptionByKey(plaintext, n, e):
        return RSA.__pow(plaintext, e, n)

    def Encryption(self, plaintext):
        return RSA.__pow(plaintext, self.e, self.n)

    @staticmethod
    def DecryptionByKey(ciphertext, n, d):
        return RSA.__pow(ciphertext, d, n)

    def Decryption(self, ciphertext):
        # Using Chinese Remainder Theorem for decryption
        Xp = ciphertext % self.p
        Xq = ciphertext % self.q
        Yp = RSA.__pow(Xp, self.Dp, self.p)
        Yq = RSA.__pow(Xq, self.Dq, self.q)
        u = (Yq - Yp) * self.t % self.q
        return Yp + self.p * u
