def SAMpow(x, n, m):
    # return x^n mod m
    binN = bin(n)[3:]
    result = x
    for i in binN:
        result = (result * result) % m
        if i == '1':
            result = (result * x) % m
    return result