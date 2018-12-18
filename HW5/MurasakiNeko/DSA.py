import random


class DSA:
    def __init__(self):
        self.p = 59
        self.q = 29
        self.a = 3
        self.d = 7
        self.b = 4
        print("Kpub:", self.p, self.q, self.a, self.b)
        print("Kpri:", self.d)

    def __ExtendGCD(self, a, b):
        if b == 0:
            return 1, 0
        else:
            x, y = self.__ExtendGCD(b, a % b)
            return y, (x - (a // b) * y)

    def __ModularInverse(self, val, mod):
        return self.__ExtendGCD(val, mod)[0] % mod

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

    def SignatureGeneration(self, Hx):
        Ke = random.randint(1, self.q)
        r = DSA.__pow(self.a, Ke, self.p) % self.q
        s = (Hx + self.d * r) * self.__ModularInverse(Ke, self.q) % self.q
        print("Signature:", r, s)
        return r, s

    def SignatureVerification(self, Hx, r, s):
        w = self.__ModularInverse(s, self.q)
        u1 = w * Hx % self.q
        u2 = w * r % self.q
        v = (pow(self.a, u1, self.p) * pow(self.b, u2, self.p)) % self.p % self.q
        print("w:", w, "u1:", u1, "u2:", u2)
        if v == r:
            print("Signature is valid.")
        else:
            print("Signature is invalid.")


dsa = DSA()
r, s = dsa.SignatureGeneration(26)
dsa.SignatureVerification(26, r, s)
