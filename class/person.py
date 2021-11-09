class Person:
    def __init__(self, name, age):
        self._person_name = name
        self._person_age = age

    @property
    def name(self):
        return self._person_name

    @name.setter
    def name(self, name):
        if name == '':
            raise Exception('not valid name')
        self._person_name = name

    @property
    def age(self):
        return self._person_age

    @age.setter
    def age(self, age):
        if age < 0:
            raise Exception('not valid age')
        self._person_age = age

    def __str__(self):
        return f'person with name {self._person_name}, and age {self._person_age}'

    def drive(self):
        print(f'{self._person_name} drives a car zhigul')
