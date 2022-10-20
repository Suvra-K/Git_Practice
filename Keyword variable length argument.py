def display(farg, **args): # **args internally represents a dictionary object
    print("farg = ",farg)
    for x,y in args.items(): # items() will give pairs of items
        print("Key= {} and Value = {}".format(x,y))

    print(args,type(args))




display(farg = 110,Name = 'Suvra')
display(farg = 10,Name = 'Suvra',age=30)


