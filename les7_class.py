import time
class Person:
    person_type = 'Python_dev'
    def __init__(self, name='Petro'):
        self.name = name
        self._private = 'secret'

    def say_name(self):
        print('My name is {}'.format(self.name))


    @staticmethod
    def print_time():
        print(time.time())

    @classmethod
    def print_person_type(cls):
        print(cls.person_type)

    def say_secret(self):
        print(self._private)

    def __del__(self):
        print('Rampage!!')

    def __str__(self):
        return 'I am{}'.format(self.name)

trainer = Person('Alexander')
#del trainer
student_1 = Person(name='Mike')
student_2 = Person('Chuck')
student_3 = Person('Valery')
student_4 = Person()

trainer.say_name()
student_3.say_name()

print(student_4.name)
print(Person.person_type)
print(student_1.person_type)

print(trainer.say_name)
print(callable(trainer.say_name))

print(trainer.say_name)
print(callable(trainer.name))

Person.print_person_type()
Person.print_time()

print(trainer._private)
trainer.say_secret()

print(dir(trainer))