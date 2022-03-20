class Animal():
    def __init__(self, animal):
        self.health = 100
        self.animal = animal

    def hit(self):
        s.health -= w.damage


class Hunter(Animal):
    def __init__(self):
        super().__init__('wolf')
        damage = int(input('wolf damage= '))
        if damage > 100:
            damage = 100
        print(damage)
        self.damage = damage


class Target(Animal):
    def __init__(self):
        super().__init__('sheep')
        pass


s = Target()

w = Hunter()
w.hit()
print(f'hp sheep= {s.health}')
