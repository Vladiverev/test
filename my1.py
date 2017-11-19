number = int(input('1.Enter your number: '))
if number%2 == 0:
    print('четное')
else:
    print('нечетное')

name = input('2.ФИО')
a=name.title()
print(a)

import math
a = int(input('3.Enter your a: '))
b = int(input('Enter your b: '))
c = int(input('Enter your c: '))
d = b**2-4*a*c
if d >= 0:
    x_1 = (-b-math.sqrt(d))/(2*a)
    x_2 = (-b+math.sqrt(d))/(2*a)
    print('x_1= x_2=')
    print(x_1, x_2)
else:
    print('Уравнение не имеет решений')