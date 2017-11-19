num = input('Vvedite nomer bileta')
a = len(num) // 2


def summa_1(num):
    summa = 0
    for i in num[:a]:
        summa += int(i)
    return summa


def summa_2(num):
    summa = 0
    for i in num[a:]:
        summa += int(i)
    return summa


b = summa_1(num)
c = summa_2(num)

num_int = int(num);

while summa_1(str(num_int)) != summa_2(str(num_int)):
    num_int += 1

print(int(num_int - int(num)))

num_int = int(num);

while summa_1(str(num_int)) != summa_2(str(num_int)):
    num_int -= 1

print(int(num) - num_int)