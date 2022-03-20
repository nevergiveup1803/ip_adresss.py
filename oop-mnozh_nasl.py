class Human:
    def __init__(self, work):
        self.work = work

    def can_breathe(self):
        return 'могу дышать'

    def can_walk(self):
        return 'могу ходить'

    def __repr__(self):
        return f'Человек - {self.work}'


class Doctor(Human):

    def can_help(self):
        return 'могу лечить'


class Teacher(Human):

    def can_teach(self):
        return ('могу учить')


d = Doctor('Доктор')
t = Teacher('Учитель')
print(d)
print(t)
print(d.work, d.can_help(), d.can_walk(), d.can_breathe())
print(t.work, t.can_teach(), t.can_walk(), t.can_breathe())
