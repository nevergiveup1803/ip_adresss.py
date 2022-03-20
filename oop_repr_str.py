class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Human object - {self.name}'

    def __str__(self):
        return f'Human - {self.name}'


human_1 = Human('Alex')
print(human_1.__repr__())
print(human_1.__str__())
