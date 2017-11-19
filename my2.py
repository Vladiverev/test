s = (str(input('text')))
x = s.count('f')
z = s.replace('f', '!')
print(z, x)



import re
s = (str(input('text')))
x = re.subn (',', '!', s)
print(x)



import math
operation = input('Выберите +,-,*,/,^,sqrt')
num_1 = int(input('Введите первое число или возводимое в степень: '))
num_2 = int(input('Введите второе число или степень: '))
if operation == '+':
        print('число 1 + число 2 = ')
        print(num_1 + num_2)
elif operation == '-':
        print('число 1 + число 2 = ')
        print(num_1 - num_2)
elif operation == '*':
        print('число 1 + число 2 = ')
        print(num_1 * num_2)
elif operation == '/':
        print('число 1 + число 2 = ')
        print(num_1 / num_2)
elif operation == '^':
        print('число 1 + число 2 = ')
        print(num_1 ** num_2)
elif operation == 'sqrt':
        print('sqrt(корень первого числа),sqrt(корень второго числа)')
        print(math.sqrt(num_1), math.sqrt(num_2))
else:
        print('Неверная функция')




