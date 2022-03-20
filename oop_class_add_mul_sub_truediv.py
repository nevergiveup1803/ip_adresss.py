class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'{self.name}, {self.balance}'

    # Возвращение нового объекта: return Bank(self.name, self.balance + other)
    def __add__(self, other):
        print('__add__')
        if isinstance(other, int):
            return Bank(self.name, self.balance + other)
        elif isinstance(other, Bank):
            return self.balance + other.balance

    def __radd__(self, other):
        print('__radd__')
        return self + other

    def __mul__(self, other):
        print('__mul__')
        if isinstance(other, int):
            return self.balance * other
        elif isinstance(other, Bank):
            return self.balance * other.balance

    def __rmul__(self, other):
        print('__rmul__')
        return self * other


alex = Bank('alex', 10000)
misha = Bank('misha', 9999)
print(misha + 1)
print(alex + misha + 1)
print(alex + 'asd')
print(123 + misha)
print(alex * 3)
print(12 * alex)
