def make_multiplier_of(n):        #zamikanie
    def multiplier(x):
        return x*n

    return multiplier

mult5 = make_multiplier_of(5)
print(mult5(10))
print(mult5(12))
print(mult5(15))

mult7=make_multiplier_of(7)
print(mult7(11))
print(mult7(20))
print(mult7(30))