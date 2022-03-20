class Vektor:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item <= len(self.values):

            return self.values[item]
        else:
            return 'Not inna range'

    def __setitem__(self, key, value):
        try:
            if 0 <= key <= len(self.values):
                self.values[key - 1] = value
            elif key > len(self.values):
                diff = key - len(self.values)
                self.values.extend('0' * diff)
                self.values[key - 1] = value
        except Exception as e:
            print(e)


    def __delitem__(self, key):
        if 0 <= key <= len(self.values):
            del self.values[key]


a = Vektor(1, 4, 3, 4, 5)
print(a)

a[50] = 100
print(a)

del a[4]
print(a)
