def named_params(*args, **kwargs):
    print(args)
    print(kwargs)


named_params(0, a=1, b=2)
