# declaration et affectation de / au variable gauche 
gauche = "/"
# declaration et affectation de \ au variable droite 
droite = "\\"
# declaration et affectation de __ au variable base
base = "__"
# declaration et affectation de la valeur saisie par l'utilisateur au variable hauteur 
hauteur = int(input("hauteur : "))
# pour i allant de 0 a la hauteur 
# affiche les deux cotés du triangle
# si i egale a hauteur -1
# affiche la base du triangle
for i in range(hauteur):
    print((hauteur - i) * " " + gauche + ((i * 2) * " ") + droite)
    if i == hauteur - 1:
        print(gauche + base * hauteur + droite)