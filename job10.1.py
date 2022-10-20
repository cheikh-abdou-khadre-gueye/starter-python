# Afficher le contenu du fichier "output.txt" dans le terminal
outputFile = open("output.txt")
text = outputFile.read()
print(text)
outputFile.close()

# with open("output.txt") as filin:
#     lignes = filin.readlines()
#     for ligne in lignes:
#         print(ligne)
