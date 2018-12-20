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
        # self.p = 59
        # self.q = 29
        # self.a = 3
        # self.d = 7
        # self.b = 4
        self.p = 89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270413618581675256167809329851578817868788150655399575107039242098647
        self.q = 985816134032337599979598317855724021856285821241
        self.a = 26814919574494647847024112448719179212299202855485337944576386689307079439864260552494188944105773145671857092773382606846302228778554192500878302097907708140724537956112697029210681268367126899194460783294171176012709920607344487973520467487690028194112908307441065344028333480496447429463796043644504722713
        self.d = 33993005981546228955019280636228931951144427432
        self.b = 34747949452834899238863212900500654966036741227672521920873910244631139302012765804452013379701418601621824753212336126907996253328115927238396471402983389060365803441363060395348525751378200617619198656867719115081698857343187802859150446742057036767116159617411319169616411022605918594914778853108415807058

    def KeyGeneration(self):
        # p, q 生成
        while True:
            self.p = 0
            self.q = Math.makePrime(160)    # 先找 160 bit 的 q

            leftLimit = pow(2, 1024 - 1)
            rightLimit = pow(2, 1024)
            x = leftLimit // self.q + 1
            i = self.q * x                      # 1024 bit 中最小的 q 倍數
            while(i < rightLimit):              # 1024 bit 內找(q 倍數 + 1)是否為質數
                if Math.isPrime(i + 1):
                    self.p = i + 1
                    break
                i += self.q
            if self.p > 0:                      # 這個 q 找不到 1024 bit 的 p
                break

        self.a = Math.pow(2, (self.p - 1) // self.q, self.p)
        self.d = random.randint(1, self.q - 1)
        self.b = Math.pow(self.a, self.b, self.p)
        print("Kpub:", self.p, self.q, self.a, self.b)
        print("Kpri:", self.d)

    def SignatureGeneration(self, x):
        hashFunc = hashlib.sha1()
        hashFunc.update(x)
        x = int(hashFunc.hexdigest(), 16)
        Ke = random.randint(2, self.q - 1)
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
