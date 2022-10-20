# déclaration et affectation de hauteur et de largeur aux variables
hauteur = int(input("hauteur: "))
largeur = int(input("largeur: ")) 
# pour H allant de 1 à hauteur +1 
# pour L allant de 1 à largeur +1
# si H est égale à hauteur et L egale à largeur ou H et L egalent a 1
# affiche "|"
#sinon si L egale à 1 ou largeur
# affiche "|"
##sinon si H egale à 1 ou hauteur
# affiche "_"
# sinon affiche ""
for H in range(1,hauteur+1):
    for L in range(1,largeur+1):
        if (H == hauteur and L == largeur) or (L==1 and H==1):
            print("|", end="")
        elif L == 1 or L == largeur:
            print("|",end="")
        elif H == 1 or H == hauteur:
            print("-", end="")
        
        else:
            print(" ", end="")
    print("")