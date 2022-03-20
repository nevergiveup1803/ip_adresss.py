class Bank_public:
    def __init__(self, balance):
        self.balance = balance

    def show_public(self):
        print(f'Balance : {self.balance}')


first_account = Bank_public(100)
first_account.show_public()
print(first_account.balance)


class Bank_protected:
    def __init__(self, balance):
        self._balance = balance

    def show_protected(self):
        print(f'Balance_protected : {self._balance}')


first_account = Bank_protected(100)
first_account.show_protected()
print(first_account._balance)


class Bank_private:
    def __init__(self, balance):
        self.__balance = balance

    def show_private(self):
        print(f'Balance_private : {self.__balance}')


first_account = Bank_private(100)
first_account.show_private()
print(first_account._Bank_private__balance)


