def myFunction( *nombre ):
    mylist = []
    for i in nombre:
        if isinstance(i,(int)):
            mylist.append(i)
    
    for j in mylist:
        if j % 2 == 0:
            print(j)

myFunction(5,10,6,15)