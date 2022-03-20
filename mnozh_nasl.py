# class Doctor:
#
#     def can_help(self):
#         print('могу помогать')
#
#     def can_walk(self):
#         print('Doctor')
#         print('могу идти')
#
#
# class Teacher:
#
#     def can_teach(self):
#         print('могу учить')
#
#     def can_walk(self):
#         print('Teacher')
#         print('могу идти')
#
#
# class Person(Teacher, Doctor):
#     def can_walk(self):
#         Teacher.can_walk(self)
#         Doctor.can_walk(self)
#
#
# p = Person()
# p.can_help()
# p.can_teach()
# print(Person.__mro__)
# p.can_walk()


class Doctor:
    def __init__(self, deegre):
        self.deegre = deegre



class Teacher:
    def __init__(self, rank):
        self.rank = rank



class Person(Teacher, Doctor):
    def __init__(self, deegre, rank):
        super().__init__(rank)
        Doctor.__init__(self, deegre)

    def __str__(self):
        return f'{self.deegre}, {self.rank}'


p = Person(5, 6)
print(p)
