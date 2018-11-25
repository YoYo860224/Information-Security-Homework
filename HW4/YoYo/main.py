import RSA
import sys

def main():
    N, e, d = RSA.GetRSAKey()

    message = 2018
    en = RSA.RSA(message, N, e)
    print(en)
    de = RSA.RSA(en, N, d)
    print(de)
    
if __name__ == "__main__":
    main()
