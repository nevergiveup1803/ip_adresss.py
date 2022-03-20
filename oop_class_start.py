import random


# Создание класса персонаж
class Character():
    '''Создание класса персонаж с несколькими атрибутами.'''
    dead_health = 0

    def __init__(self, race, damage, age, name):
        self._race = race
        self._damage = damage
        self._age = age
        self.health = 115
        self.name = name

    @property
    def age(self):
        return self._age

    def hit_elf(self, damage):
        rnd = random.randint(-5, 5)
        ork_1.health -= damage + rnd
        print(f'damage Elf - {damage + rnd}')

    def hit_ork(self, damage):
        rnd = random.randint(-5, 5)
        elf_1.health -= damage + rnd
        print(f'damage Ork - {damage + rnd}')

    def is_dead_elf(self):
        if elf_1.health <= Character.dead_health:
            print('Elf is dead')

    def is_dead_ork(self):
        if ork_1.health <= Character.dead_health:
            print('Ork is dead')


elf_1 = Character('Elf', 30, 25, 'Nepobedimai')
print(f'race: {elf_1._race}, name - {elf_1.name}')
ork_1 = Character('Ork', 15, 63, 'Grewqfqwe')
ork_1.health = 200
print(f'race: {ork_1._race}, name - {ork_1.name}')
iteration = 1
print(f'HP Elf: {elf_1.health}')
print(f'HP Ork: {ork_1.health}')
while elf_1.health > 0 and ork_1.health > 0:
    print(f'Round: {iteration}')

    elf_1.hit_elf(elf_1._damage)
    ork_1.hit_ork(ork_1._damage)
    if elf_1.health <= 0 or ork_1.health <= 0:
        break
    print(f'HP Elf: {elf_1.health}')
    print(f'HP Ork: {ork_1.health}')
    iteration += 1
elf_1.is_dead_elf()
ork_1.is_dead_ork()
