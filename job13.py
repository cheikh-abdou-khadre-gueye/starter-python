# declaration et affectation du nombre de lettre saisis a nbl
nbl = int(input("Nombre de lettres: "))
# declaration et initialisation de la variable mots a 0
mots = 0
#ouvrir un fichier et l'affectation a la variable file
with open("data.txt", "r") as file:
    
#lis toutes les chaines de caracteres du fichier

    lignes = file.read()

#liste chaque mot dans une liste    
    liste = lignes.split()

#compte le nombre de mot si égal à l'entrée utilisateur 
    for n in liste:
        if len(n) == nbl:
            mots += 1
# afficher le nombre de mots
print(mots)