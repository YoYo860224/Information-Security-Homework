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


class DSA:
    def __init__(self):
        self.p = 59
        self.q = 29
        self.a = 3
        self.d = 7
        self.b = 4
        # self.p = 89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270413618581675256883102724335589335116634917631823889786020221276369
        # self.q = 1316000349009119659071359514621645125183937169577
        # self.a = 56962729350251973072708382160355230095382064032784692675006372684462035899723600096683758707292589475121840430732234527069546417885198143182896607336977575805236807499700705236608617345163308231760635948742924569924028084203642909225044133517132906090032989138823786726484233105901884598823767668031189916389
        # self.d = 47609914610636033929406820546224972605051023098723817782349104073685062182246497982236599682201955315532468925665905325103972391172455099216151279150254836536208371866402962899500072691271661330984147691593546427217421397533210839275244949838177355281696530474518752051997486519324535433564421900113710867510
        # self.b = 1102568376356344783630926367745025260170829125728

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
        self.b = Math.pow(self.a, self.d, self.p)
        print("Kpub:", self.p, self.q, self.a, self.b)
        print("Kpri:", self.d)

    def SignatureGeneration(self, x):
        hashFunc = hashlib.sha1()
        hashFunc.update(x)
        x = int(hashFunc.hexdigest(), 16)
        r = 0
        s = 0
        while r == 0 or s == 0:
            Ke = random.randint(2, self.q - 1)
            r = Math.pow(self.a, Ke, self.p) % self.q
            s = ((x + self.d * r) * Math.pow(Ke, self.q - 2, self.q)) % self.q
        print("Signature:", r, s)
        return r, s

    def SignatureVerification(self, x, r, s):
        hashFunc = hashlib.sha1()
        hashFunc.update(x)
        w = Math.pow(s, self.q - 2, self.q)
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
