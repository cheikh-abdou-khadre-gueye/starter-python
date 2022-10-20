# declaration et affectation d'untexte a la variable text
text = input("saisi un texte ")
# declaration et affectation d'un fichier ouvert a la variable filout
with open("output.txt", "w") as filout:
# ecriture d'un texte dans le fichier output.txt
    filout.write(text)