def fibonacci():
    a, b = 0, 1

    while True:
        yield b

        a, b = b, a + b

fib = fibonacci()
print(type(fib))

for i in fib:
    print(',', i)