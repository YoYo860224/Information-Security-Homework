import random
import hashlib
from datetime import datetime


class Math:
    @staticmethod
    def __MillerRabinTest(N):
        k = 0
        m = N - 1
        while m % 2 == 0:
            m //= 2
            k += 1
        a = random.randint(2, N - 2)
        b = pow(a, m, N)
        if b != 1 and b != N - 1:
            i = 1
            while i < k and b != N - 1:
                b = b * b % N
                if b == 1:
                    return False
                i += 1
            if b != N - 1:
                return False
        return True

    @staticmethod
    def isPrime(N):
        for times in range(10):
            result = Math.__MillerRabinTest(N)
            if not result:
                return False
        return True

    @staticmethod
    def __ExtendGCD(a, b):
        if b == 0:
            return 1, 0
        else:
            x, y = Math.__ExtendGCD(b, a % b)
            return y, (x - (a // b) * y)

    @staticmethod
    def makePrime(bits):
        used = []
        while True:
            N = pow(2, bits - 1) + 1
            for times in range(1, bits - 1):
                N += 0 if random.random() < 0.5 else pow(2, times)
            if not N in used and Math.isPrime(N):
                return N
            else:
                used.append(N)

    @staticmethod
    def pow(x, y, z):
        # Square & multiply
        output = 1
        for bit in bin(y)[2:]:
            output *= output
            if bit == "1":
                output *= x
            output %= z
        return output

    @staticmethod
    def ModularInverse(val, mod):
        return Math.__ExtendGCD(val, mod)[0] % mod


class DSA:
    def __init__(self):
        self.p = 59
        self.q = 29
        self.a = 3
        self.d = 7
        self.b = 4

    def KeyGeneration(self):
        self.q = Math.makePrime(160)
        while True:
            self.p = Math.makePrime(1024)
            if (self.p - 1) % self.q == 0:
                break
        # self.p = 59
        # while True:
        #     self.q = Math.makePrime(5)
        #     if (self.p - 1) % self.q == 0:
        #         break
        self.a = Math.pow(2, (self.p - 1) // self.q, self.p)
        self.d = random.randint(1, self.q)
        self.b = Math.pow(self.a, self.b, self.p)
        print("Kpub:", self.p, self.q, self.a, self.b)
        print("Kpri:", self.d)

    def SignatureGeneration(self, x):
        hashFunc = hashlib.sha1()
        hashFunc.update(x)
        x = int(hashFunc.hexdigest(), 16)
        Ke = random.randint(1, self.q)
        r = Math.pow(self.a, Ke, self.p) % self.q
        s = (x + self.d * r) * Math.ModularInverse(Ke, self.q) % self.q
        print("Signature:", r, s)
        return r, s

    def SignatureVerification(self, x, r, s):
        hashFunc = hashlib.sha1()
        hashFunc.update(x)
        w = Math.ModularInverse(s, self.q)
        u1 = w * int(hashFunc.hexdigest(), 16) % self.q
        u2 = w * r % self.q
        v = (pow(self.a, u1, self.p) * pow(self.b, u2, self.p)) % self.p % self.q
        print("w:", w, "u1:", u1, "u2:", u2)
        if v == r:
            print("Signature is valid.")
        else:
            print("Signature is invalid.")


random.seed(datetime.now())
dsa = DSA()
dsa.KeyGeneration()
r, s = dsa.SignatureGeneration(b"myDSAbooo")
dsa.SignatureVerification(b"myDSAbooo", r, s)
