class DES:
    def __init__(self):
        self.IP = []
        self.IP += [58, 50, 42, 34, 26, 18, 10, 2]
        self.IP += [60, 52, 44, 36, 28, 20, 12, 4]
        self.IP += [62, 54, 46, 38, 30, 22, 14, 6]
        self.IP += [64, 56, 48, 40, 32, 24, 16, 8]
        self.IP += [57, 49, 41, 33, 25, 17, 9, 1]
        self.IP += [59, 51, 43, 35, 27, 19, 11, 3]
        self.IP += [61, 53, 45, 37, 29, 21, 13, 5]
        self.IP += [63, 55, 47, 39, 31, 23, 15, 7]
        # for index in range(0, len(self.IP), 8):
        #     print(self.IP[index:index + 8])

        self.IPInverse = [-1] * len(self.IP)
        for index in range(len(self.IP)):
            self.IPInverse[self.IP[index] - 1] = index + 1
        # for index in range(0, len(self.IPInverse), 8):
        #     print(self.IPInverse[index:index + 8])

        self.E = [(start + index) % 32 + 1 for start in range(-1, 28, 4) for index in range(6)]
        for index in range(0, len(self.E), 6):
            print(self.E[index:index + 6])


des = DES()
