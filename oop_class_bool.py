class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __bool__(self):
        print('__bool__')
        return self.x != 0 or self.y != 0

    def __len__(self):
        print('__len__')
        return abs(self.x - self.y)


t1 = Point(1, 0)
if t1:
    print('hi')
    print('True')

else:
    print('no hi')
    print('False')


