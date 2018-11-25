import math

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

def GetRSAKey(p, q):
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

# 加解密過程
# 明文 p, 密文 c
# c = p^e (mod N)
# p = c^d (mod N)
    # p = p^(d*e)           (mod N)
    #   = p^(n*r + 1)       (mod N)
    #   = p^(phi(N))^n * p  (mod N)
    #   = 1^n * p           (mod N)
    #   = p
# 因為(mod N) 的關係  明文密文限制在 N 以下的值
def RSA(message, N, key):
    if message < N:
        return pow(message, key, N)
    else:
        raise Exception('message >= N')






