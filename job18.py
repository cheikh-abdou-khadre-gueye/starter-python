def myFunction( *nombre ):
    mylist = []
    for i in nombre:
        if isinstance(i,(int)):
            mylist.append(i)
            mylist.sort()
    print(mylist)

myFunction(5,10,6,15,56,84,42,2,40)