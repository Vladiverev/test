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


class Student(Person):
    def __init__(self, name, lang):
        super().__init__(name)
        self.language = lang

    def show_specialization(self):
        print(self.language)

student_x = Student('Alex', 'Python')
student_x.say_name()
student_x.show_specialization()