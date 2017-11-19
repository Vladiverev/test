# generator

def my_generator(val):
    while val > 0:
        val -= 1
        yield val
        # return val

gen = my_generator(5)
print(type(gen))


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))