from person import Person
from major import Major

def greet(person: Person):
    print(f'greetings, {person.name}!!!')

def greet_major(person: Major):
    print(f'hello major, {person.name}, your balance is {person.money}!!!')




person1 = Person('ivan', 18)
print(person1)
major1 = Major('petr', 12, 1000)
# print(major1)
# # greet(person1)
# # greet(major1)
# # greet_major(major1)
# greet_major(person1)
# print(isinstance(person1, Major))
# print(isinstance(major1, Person))
major1.drive()
person2 = Person
print(type(person2))
print(type(person1))
print(type(True))
print(person2)
