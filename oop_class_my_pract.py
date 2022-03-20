class Car:
    model = 'audi'

    def drive(self, model):
        print('vroom', model)


cat_1 = Car()
cat_1.drive(cat_1.model)


class Cat:
    __shared_attr = {
        'por': 'siam',
        'color': 'black',
        'age': '8'

    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr


cat_1 = Cat()
print(cat_1.__dict__)
cat_1.por = 'pers'
print(cat_1.__dict__)
cat_1.color = 'white'
cat_1.age = 10
cat_2 = Cat()