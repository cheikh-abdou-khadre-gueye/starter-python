# pour i allant de 1 à 101 
for i in range(1,101) :
# si la valeur de i est multiple de 3 et de 5 affiche FizzBuzz 
    if i%3 == 0 and i%5 == 0 :
        print("FizzBuzz")
# si seulement la valeur de i est multiple de 3 afficher Fizz
    elif i%3 == 0 : 
        print("Fizz")
# si seulement la valeur de i est multiple de 5 afficher Bizz
    elif i%5 == 0 :
        print("buzz")
    else:
# sinon afficher valeur n'est pas multiple de 3 ni de 5
        print(i,"n'est pas multiple par 3 ni par 5")