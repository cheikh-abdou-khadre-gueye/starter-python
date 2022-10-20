# déclaration et affectation de valeur à une variable
chevron = input(">")
# si la valeur saisie est egale a bonjour afficher bonjour à toi 
if chevron == "Bonjour" :
    print("Bonjour à toi")
# si la valeur saisie est egale à au revoir quitte le programme
elif chevron == "Au revoir" :
    quit()
# sinon affiche la valeur saisie      
else : print(chevron)