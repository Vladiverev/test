def with_global():
    global a
    a = 2
    print(a)
    nonlocal b
     b = 2

with_global()
print(a)