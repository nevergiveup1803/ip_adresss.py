class Pryamougol:
    __slots__ = 'vis', 'shir'

    def __init__(self, a, b):
        self.vis = a
        self.shir = b


p = Pryamougol(1, 2)
print(p.vis, p.shir)
