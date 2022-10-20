# déclaration et affectation de valeur à une variable 
val1 = int(input("valeur 1 "))
# déclaration et affectation de valeur à une variable 
val2 = int(input("valeur 2 "))
# si la deuxieme valeur est supperieur au premiere afficher les valeurs entre val1 et val2 d'une maniere croissante
if (val1 < val2):
    for i in range(val1+1,val2):
        print(i)
# si la deuxieme valeur est supperieur au premiere afficher les valeurs entre val1 et val2 d'une maniere décroissante
elif (val1 > val2):
    for i in range(val1-1,val2,-1):
        print(i)
else:
# sinon afficher valeurs egales
    print("valeurs egales")
