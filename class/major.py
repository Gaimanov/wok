from person import Person

class Major(Person):
    def __init__(self, name, age, money):
        super().__init__(name, age)
        self._money = money

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money):
        if money < 0:
            raise Exception('not valid amount of money')
        self._money = money


    def drive(self):
        # print(f'{self._person_name} drives a car BMW')
        super().drive()
        print(f'with {self._money}$')

    def __str__(self):
        return f'major with name {self._person_name}, age {self._person_age} and {self._money}$'
