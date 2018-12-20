import random
import hashlib

class MyMath:
    @staticmethod
    def SAMpow(x, n, m):
        # return x^n mod m
        binN = bin(n)[3:]
        result = x
        for i in binN:
            result = (result * result) % m
            if i == '1':
                result = (result * x) % m
        return result

    @staticmethod
    def MLTest(n):
        # 必然的，Miller–Rabin 不處理 
        if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
            return False
        if n==2 or n==3 or n==5 or n==7:
            return True

        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1

        def EulerTry(a):
            r = MyMath.SAMpow(a, d, n)
            if r == 1 or r == n - 1:
                return True
            for _ in range(s - 1):
                r = (r ** 2) % n
                if r == n - 1:
                    return True
            return False
        
        # 多找幾個 a 做測試
        for _ in range(8):
            a = random.randrange(2, n)
            if not EulerTry(a):
                return False
    
        return True

    @staticmethod
    def RandomPrime(nOfBit):
        leftLimit = pow(2, nOfBit - 1) + 1
        rightLimit = pow(2, nOfBit)
        n = random.randrange(leftLimit, rightLimit, 2)
        while(MyMath.MLTest(n) != True):
            n = random.randrange(leftLimit, rightLimit, 2)
        return n

    @staticmethod
    def egcd(a, b):
        # return (gcd, x, y)
        # gcd(a, b) = a*x + b*y
        # 使用輾轉相除法
        if a == 0:
            return (b, 0, 1)
        else:
            # gcd( a,  b) =   a   * x1 + b * y1
            # gcd(b%a, a) = (b%a) * x2 + a * y2
            # gcd(a, b) = gcd(b%a, a)
            # a*x1 + b*y1 = (b%a)*x2 + a*y2 
            #             = (b - (b // a) * a) * x2 + a*y2
            #             = b*x2 - (b // a) * a * x2 + a*y2
            # let y1 = x2 => a*x1 = - (b // a) * a * x2 + a*y2
            #  => x1 = y2 - (b // a) * x2
            g, x2, y2 = MyMath.egcd(b % a, a)
            return (g, y2 - (b//a) * x2, x2)
            #      (g,       x1      , y1) 

    @staticmethod
    def modInv(a, m):
        (g, x, y) = MyMath.egcd(a, m)
        # ax + my = 1
        # ax  (mod m) = 1  (mod m)
        if g == 1:
            return x % m
        else:
            raise Exception('modular inverse does not exist')

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
            self.q = MyMath.RandomPrime(160)    # 先找 160 bit 的 q

            leftLimit = pow(2, 1024 - 1)
            rightLimit = pow(2, 1024)
            x = leftLimit // self.q + 1
            i = self.q * x                      # 1024 bit 中最小的 q 倍數
            while(i < rightLimit):              # 1024 bit 內找(q 倍數 + 1)是否為質數
                if MyMath.MLTest(i + 1):
                    self.p = i + 1
                    break
                i += self.q
            if self.p > 0:                      # 這個 q 找不到 1024 bit 的 p
                break

        self.a = MyMath.SAMpow(2, (self.p - 1) // self.q, self.p)   # a ^ q mod p = 1
        self.d = random.randint(1, self.q)                          # priKey -> d 亂數
        self.b = MyMath.SAMpow(self.a, self.d, self.p)              # pubKey -> b = a ^ d mod p
        print("Kpub-p:", self.p)
        print("Kpub-q:", self.q)
        print("Kpub-a:", self.a)
        print("Kpub-b:", self.b)
        print("Kpri-d:", self.d)

    # 以下用到
    # a ^ -1 mod p <=> a ^ (p - 2) mod p
    # a ^  0 mod p <=> a ^ (p - 1) mod p = 1 (By 歐拉)

    def SignatureGeneration(self, x):
        # message is x, 對他簽名
        hashFunc = hashlib.sha1()
        hashFunc.update(x)
        Hx = int(hashFunc.hexdigest(), 16)                                          # Hash(x)
        Ke = random.randint(1, self.q - 1)                                          # 暫時的亂數
        r = MyMath.SAMpow(self.a, Ke, self.p) % self.q                              # r = (a ^ ke mod p) mod q
        s = ((Hx + self.d * r) * MyMath.SAMpow(Ke, self.q - 2, self.q)) % self.q    # (Hash(x) + d * r)(Ke ^ -1) mod q
        return r, s


    def SignatureVerification(self, x, r, s):
        hashFunc = hashlib.sha1()
        hashFunc.update(x)
        Hx = int(hashFunc.hexdigest(), 16)                                          # Hash(x)
        w = MyMath.SAMpow(s, self.q-2, self.q)                                      # w = s ^ -1 mod q
        u1 = (w * Hx) % self.q                                                      # u1 = (w * Hx) % q 
        u2 = (w * r) % self.q                                                       # u2 = (w * r) % q

        # v = ((a ^ u1 * b ^ u2) mod p) mod q 
        v = ((MyMath.SAMpow(self.a, u1, self.p) * MyMath.SAMpow(self.b, u2, self.p)) % self.p) % self.q

        # 驗章
        if v == r:
            print('good')
        else:
            print('bad')

dsa = DSA()
dsa.KeyGeneration()
r, s = dsa.SignatureGeneration(b"myDSAbooo")
dsa.SignatureVerification(b"myDSAbooo", r, s)
