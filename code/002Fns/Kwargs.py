def random_func(*args, **kwargs):
    print(args)
    print(kwargs)
    for key in kwargs:
        print(key, "=", kwargs[key])

#caller code
random_func(1,2,3,4, name="bp", city="faridabad")