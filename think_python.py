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

if b == c:
    print('udacha', num, b, c)
else:
    print('udacha cherez =', num)




from PIL import Image
from py_tesserocr import tesserocr

img = Image.open('./data/capcha2.png')
img = img.convert('L')
img.save('./data/capcha6.tiff')

print(tesserocr.tesseract_version())
print(tesserocr.get_languages())

image = Image.open('./data/capcha6.tiff')

# tesseract ./text.png -l eng out --tessdata-dir /usr/share/tesseract-ocr/tessdata/

i = 0
while i < 11:
    print(tesserocr.image_to_text(image, lang='eng', psm=i))
    i += 1

# raspoznavanie

from py_tesserocr import tesserocr
from PIL import Image

print(tesserocr.tesseract_version())
print(tesserocr.get_languages())

image = Image.open('./data/capcha5.png')



# tesseract ./text.png -l eng out --tessdata-dir /usr/share/tesseract-ocr/tessdata/

i = 0
while i < 11:
    print(tesserocr.image_to_text(image, lang='eng', psm=i))
    i += 1

### image-> net.obraz


from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

client_id = 'Ba4KbJbr1aECLFxZKGrjzFwaUB2nqe1iyV3KYEbT'
client_secret = 'Ras3R23sfsYC1xVZK4RzxrrX2lJrzKWNAwssz2aDYoFuewsEL9'

oauth = OAuth2Session(client=BackendApplicationClient(client_id))
token = oauth.fetch_token(token_url='https://api.everypixel.com/oauth/token', auth=(client_id, client_secret))

api = OAuth2Session(client_id, token=token)

data = {'data': open('./data/p.jpg', 'rb')}
result = api.post('https://api.everypixel.com/v1/keywords', files=data).json()

for item in result['keywords']:
    print(item['keyword'])
#sql
print("Hello %s" % "John")

import pymysql


DB = pymysql.connect(host='localhost',
                      user='root',
                      password='1',
                      db='my_db',
                      cursorclass=pymysql.cursors.DictCursor)

try:
    with DB.cursor() as cursor:
        sql = "SELECT * FROM `users`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    DB.close()


# uchebnik

def right_justify(s):  # 3.3
    while len(s) < 75:
        s = ' ' + s
    else:
        print(s)


right_justify('allen')


# 3.4
def do_twice(f, arg):
    f(arg)
    f(arg)


def print_twice(arg):
    print(arg)
    print(arg)


do_twice(print_twice, 'spam')
print('')


def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)


do_four(print_twice, 'spam')
print('')


# 3.5
def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print('+ - - - -', end=" ")


def print_post():
    print('|        ', end=' ')


def print_beams():
    do_twice(print_beam)
    print('+')


def print_posts():
    do_twice(print_post)
    print('|')


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()


def one_four_one(f, g, h):
    f()
    do_four(g)
    h()


def print_plus():
    print('+', end='')


def print_dash():
    print('-', end='')


def print_bar():
    print('|', end='')


def print_space():
    print(' ', end='')


def print_end():
    print()


def nothing():
    "do nothing"


def print1beam():
    one_four_one(nothing, print_dash, print_plus)


def print1post():
    one_four_one(nothing, print_space, print_bar)


def print4beams():
    one_four_one(print_plus, print1beam, print_end)


def print4posts():
    one_four_one(print_bar, print1post, print_end)


def print_row():
    one_four_one(nothing, print4posts, print4beams)


def print_grid():
    one_four_one(print4beams, print_row, nothing)


print_grid()


# 5.1

def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print('ferma ne prav')
    else:
        print('ferma prav')


check_fermat(a=int(input('a\n')), b=int(input('b')), c=int(input('c')), n=int(input('n')))


# 5.2


def is_triangle(a, b, c):
    print(a + b)
    print(c)
    if a + b == c:
        print('Da')
    else:
        print('Net')


is_triangle(a=int(input('a')), b=int(input('b')), c=int(input('c')))


# 6.1

def compare(x, y):
    if x > y:
        print('1')
    elif x == y:
        print('0')
    elif x < y:
        print('1')


compare(x=float(input('x')), y=float(input('y')))


# 6.3

def is_between(x, y, z):
    return bool(x <= y <= z)


is_between(int(input('')), int(input('')), int(input('')))


# 6.4
def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))


print(ack(3, 4))

### 6.6 (A)

def reverse(incoming_string):
    temp_str = str('')
    str_len = len(incoming_string)

    while str_len:
        temp_str += incoming_string[str_len - 1]
        str_len -= 1


    return temp_str


def check_pali(value):
    return True if reverse(value) == value else False


print(check_pali(input()))
#6.6
def revers(a):
    return True if a == a[::-1] else False


print(revers(input('vvedite slovo\n')))

#6.7


def is_power(a, b):
    return True if a % b == 0 else False


print(is_power(int(input('a')), int(input('b'))))


def gcd(a, b):
    while a and b:
        if a > b:
            a = a % b
        else:
            b = b % a
    return int(a + b)


a = input('a= ')
b = input('b= ')
try:
    a = int(a)
    b = int(b)
except ValueError:
    print('ne chislo')
finally:
    exit()
res_a_b_gcd = gcd(a, b)
print(res_a_b_gcd)
print('Evclid\'s test was passed' if res_a_b_gcd == gcd(b, res_a_b_gcd) else "Evclid\'s test was not passed")


