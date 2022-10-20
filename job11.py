# compteur initialiser a 0
count = 0
# declaration et affectation d'un fichier ouvert par la variable filin
with open("domains.xml") as filin:
# récuperation et affectation  du contenu du fichier par la variable lignes    
    lignes = filin.readlines()
# pour ligne parcourt tout le fichier    
    for ligne in lignes:
# transformer le contenu du fichier en une liste et affecter la liste a splitLine                
        splitLine = ligne.split("\"")
# pour word parcourt toute la liste et si word egale domain compter        
        for word in splitLine:
            if word == "domain":
                count += 1

# afficher le nombre de domain trouver
print("il y a " + str(count) + " domains")
                
