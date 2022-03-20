class Animal():
    def health(self):
        print('animal')


class Hunter(Animal):
    def health(self):
        super().health()
        print('hunter')


class Target(Animal):
    def health(self):
        super().health()
        print('target')


class Dog(Target, Hunter):
    def health(self):
        super().health()
        print('dog')


dog = Dog()
dog.health()
