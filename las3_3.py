def func(a):
    print(id(a))
    a.append(2)
    print(a)

a = [1,]
print(id(a))
func(a)
print(a)


x = 1
print(id(x))
x += 2
print(id(x))

s = 'hello'
print(id(s))
s += 'world!'
print(id(s))
'{}{}{}{}{}'.format()

y=[1, ]
print(id(y))
y.append(2)
print(id(id(y)))