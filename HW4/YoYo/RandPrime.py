import random
from SquareAndMultiply import SAMpow

def MLTest(n):
    # 必然的，Miller–Rabin 不處理 
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
    if n==2 or n==3 or n==5 or n==7:
        return True

    # 引述定理
    #  x^2 =   1 (mod p)
    #   x  = +-1 (mod p)
    # 證明
    #    x^2 - 1     = 0 (mod p)
    # (x + 1)(x - 1) = 0 (mod p)
    # => x + 1 =   0 (mod p) or x - 1 = 0 (mod p) 
    # =>   x   = +-1 (mod p)

    # 根據歐拉定理來測試
    # a^(p - 1) = 1 (mod p)
    # p - 1 可分解成 (2^s)*d
    # 令 i = s-1 ~ 0, a^(2^i)*d mod p 應出現 1 直到 -1 為止
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    def EulerTry(a):
        r = SAMpow(a, d, n)
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

def RandomPrime(nOfBit):
    leftLimit = pow(2, nOfBit - 1) + 1
    rightLimit = pow(2, nOfBit)
    n = random.randrange(leftLimit, rightLimit, 2)
    while(MLTest(n) != True):
        n = random.randrange(leftLimit, rightLimit, 2)
    return n