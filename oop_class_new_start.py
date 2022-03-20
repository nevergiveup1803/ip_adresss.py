class Person:
    name = 'Aleksandr'
    age = 21


# методы обращения к атрибутам класса Person
print(getattr(Person, 'age'))

Person.name = 'Onyx'
print(getattr(Person, 'name'))

setattr(Person, 'name', 'John')
print(getattr(Person, 'name'))

setattr(Person, 'address', '12 ST')
print(getattr(Person, 'address'))

delattr(Person, 'address')



person_1 = Person()
person_1.name = 'Aleksandr'
print(person_1.name)
print(Person.name)
print(person_1.__dict__)
