# Importer RegEx
import re
# ouverture et affectation du fichier data.txt a la variable fichier
fichier = open("data.txt", "r")
# utilisation de la methode re.findall pour qu'elle renvoie une liste de chaînes dans l'ordre correspondant
mots = re.findall('[a-zA-Z]+', fichier.read())
# declaration et affectation du nombre de mot a la variable nombre_de_mots
nombre_de_mots = len(mots)
# fermer le fichier data.txt
fichier.close()
# afficher le nombre mot dans le fichier data.txt
print(nombre_de_mots)
