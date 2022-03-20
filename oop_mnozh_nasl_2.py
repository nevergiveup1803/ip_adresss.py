class Animal():

    def __init__(self):
        self.health = 100

    def hit(self, damage):
        self.health -= damage


class Hunter(Animal):
    def __init__(self):
        super().__init__()
        # Animal.__init__(self)
        self.legs = 4


h = Hunter()
h.hit(40)
print(h.health)
