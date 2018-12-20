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
        self.d = random.randint(1, self.q)                          # d 亂數
        self.b = MyMath.SAMpow(self.a, self.b, self.p)              # b = a ^ d mod p
        print("Kpub-p:", self.p)
        print("Kpub-q:", self.q)
        print("Kpub-a:", self.a)
        print("Kpub-b:", self.b)
        print("Kpri-d:", self.d)

dsa = DSA()
dsa.KeyGeneration()
