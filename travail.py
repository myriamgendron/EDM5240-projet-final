#!/usr/bin/env python
# coding: utf-8 
import enchant
dictionnaire = enchant.Dict("fr_FR")

texteAvant = open("avant.txt", "r").read().split() # TODO Trouver un moyen de lire plusieurs fichiers
texteApres = open("apres.txt", "r").read().split()

if len(texteAvant) != len(texteApres): # TODO Trouver un moyen lorsque les textes n'ont pas la même longueur. (ex.: comparer les mots suivants)
    print("Les textes doivent être de la même longueur")
    exit()

bonsMots = 0
mauvaisMots = 0
virgules = 0
orthographes = 0
accords = 0
motsChanges = 0

for index in range(len(texteAvant)):
    motApres = texteApres[index]
    motAvant = texteAvant[index]
    if motAvant == motApres:
        bonsMots += 1
    else:
        mauvaisMots += 1
        if "," in motApres and "," not in motAvant:
            virgules += 1
            motApres = motApres[:-1]
        
        mauvaisMotsPropre = motAvant.replace(",", "")
        if not dictionnaire.check(motAvant):
            orthographes += 1
        elif motApres.endswith("s") and not motAvant.endswith("s"):
            accords += 1
        elif motApres.endswith("e") and not motAvant.endswith("e"):
            accords += 1
        elif motApres.endswith("x") and not motAvant.endswith("x"):
            accords += 1
        elif motApres.endswith("ent") and not motAvant.endswith("ent"):
            accords += 1
        elif motApres.endswith("ont") and not motAvant.endswith("ont"):
            accords += 1
        else:
            motsChanges += 1


print("========  Statistiques  ==============")
print("Nombre de bons mots: " + str(bonsMots))
print("Nombre de mots mal écrits: " + str(mauvaisMots))
print("     Virgules manquantes:" + str(virgules))
print("     Orthographes manquantes:" + str(orthographes))
print("     Mauvais accord:" + str(accords))
print("     Mots changés:" + str(motsChanges))
