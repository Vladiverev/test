def complex_funktion(*args):
    for x in args:
        if callable(x):
            x()

        else:
            print(x)


def func1():
    print('From funkion 1')


def func2():
    print('From funktion 2')
    return "From 2"


complex_funktion('a', 1, 2, func1, func2())
