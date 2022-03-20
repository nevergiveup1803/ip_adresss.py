class Kv:
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2


class Pr:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Krug:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2


k = Kv(10)
p = Pr(5, 10)
kr = Krug(10)
print(k.area())
print(p.area())
print(kr.area())
# Полиморфизм.
for figure in [k, p, kr]:
    print(figure.area())
