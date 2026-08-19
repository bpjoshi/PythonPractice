def catalogue(name, *args):
    print(name)
    print("type of args:", type(args))
    #type of args: <class 'tuple'> : a non modifiable array
    for value in args:
        print(value)
    if len(args)>=1:
        print(args[0])

catalogue("movies", "LOTR", "HPS", "TROY")