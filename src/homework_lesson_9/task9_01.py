class Snow:
    def __init__(self, n):
        self.n = n

    def __add__(self, n):
        self.n += n
        return self.n

    def __mul__(self, n):
        self.n *= n
        return self.n

    def __sub__(self, n):
        self.n -= n
        return self.n

    def __truediv__(self, n):
        self.n /= n
        return round(self.n)

    def make_snow(self, m):
        snow_str = ""
        for j in range((int(self.n) + m) + 1):
            snow_str += m * '*'
            snow_str += "\n"
        print(snow_str)
        # Второй вариант метода:
        # for i in range((int(self.n) + m) + 1):
        #     print(i, m * '*')


snowfall = Snow(10)
print(snowfall.__add__(10))
print(snowfall.__sub__(5))
print(snowfall.__mul__(2))
print(snowfall.__truediv__(4))
snowfall.make_snow(20)
