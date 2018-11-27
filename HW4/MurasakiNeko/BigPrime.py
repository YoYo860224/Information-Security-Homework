import random


class BigPrime:
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
    def __isPrime(N):
        for times in range(20):
            result = BigPrime.__MillerRabinTest(N)
            if not result:
                return False
        return True

    @staticmethod
    def makePrime(bits):
        while True:
            N = pow(2, bits - 1) + 1
            for times in range(1, bits - 2):
                N += 0 if random.random() < 0.5 else pow(2, times)
            if BigPrime.__isPrime(N):
                return N
