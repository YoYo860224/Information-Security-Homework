import math
import RandPrime
from SquareAndMultiply import SAMpow

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
        g, x2, y2 = egcd(b % a, a)
        return (g, y2 - (b//a) * x2, x2)
        #      (g,       x1      , y1) 

def modInv(a, m):
    (g, x, y) = egcd(a, m)
    # ax + my = 1
    # ax  (mod m) = 1  (mod m)
    if g == 1:
        return x % m
    else:
        raise Exception('modular inverse does not exist')

def GetRSAKeyByPrime(p, q):
    # 選兩個大質數
    N = p * q

    # phi(N) = r = (p - 1) * (q - 1)
        # r = p*q - p - q + 1
    # 求得與 r 互質的 e
    # 求得 d 使得 e*d mod r = 1 
        # e*d = n*r + 1
    r = (p - 1) * (q - 1)
    e = 0
    for i in (range(2, r)):
        if math.gcd(i, r) == 1:
            e = i
            break
    d = modInv(e, r)
    return N, e, d

def GetRSAKeyByBit(NumOfBit):
    oneOfThat = NumOfBit // 2
    p = RandPrime.RandomPrime(oneOfThat)
    q = RandPrime.RandomPrime(oneOfThat + 1)

    N, e, d = GetRSAKeyByPrime(p, q)

    return N, e, d, p, q

# 加解密過程
# 明文 p, 密文 c
# c = p^e (mod N)
# p = c^d (mod N)
    # p = p^(d*e)           (mod N)
    #   = p^(n*r + 1)       (mod N)
    #   = p^(phi(N))^n * p  (mod N)
    #   = 1^n * p           (mod N)
    #   = p
# 因為(mod N) 的關係  明文密文限制在 N bits 以下的值

def RSA(message, N, key):
    if message < N:
        return SAMpow(message, key, N)
    else:
        raise Exception('message >= N')

def RSAbyCRT(message, N, key, p, q):
    # CRT: 中國餘式定理
    # x % m1 = a1
    # x % m2 = a2
    # M = m1 * m2
    # M1 = m2
    # M2 = m1
    # 求 ti, 使 ti * Mi % mi = 1
    # x = a1 * t1 * M1 + a2 * t2 * M2 + kM

    # CRT in RSA
    # plain = message ^ key % N
    # 令 a1 = message ^ key % p
    # 令 a2 = message ^ key % q
        # a1, a2 可用歐拉定理加速運算
        # m ^ k % p
        # => m ^ (n * (p-1) + r) % p
        # => m ^ (n * (p-1)) % p * m ^ r % p
        # => m ^ r % p
        # 其中 r = k % (p-1)
    a1 = SAMpow(message, key % (p-1), p)
    a2 = SAMpow(message, key % (q-1), q)

    # 最後運用中國餘式定理求 plain
    # x % p = a1
    # x % q = a2
    # M = p * q = N
    # plain = x % M, 最小 x 解
    m1 = p
    m2 = q
    M1 = m2
    M2 = m1
    t1 = modInv(M1, m1)
    t2 = modInv(M2, m2)
    return (a1 * t1 * M1 + a2 * t2 * M2) % N
