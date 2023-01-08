# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import argparse
def simuler_etapes(niveaux_energie, etapes):
    # Récupère le nombre de lignes et de colonnes de la matrice niveaux_energie
    lignes = len(niveaux_energie)
    colonnes = len(niveaux_energie[0])
    # Initialise un compteur pour compter les octopus qui clignotent
    clignote = 0
    for _ in range(etapes):
        #Augmenter le niveau d’énergie de chaque octopus de 1
        niveaux_energie = [[e+1 for e in row] for row in niveaux_energie]
        # Trouver les octopus qui clignotent
        clignotant = [[False] * colonnes for _ in range(lignes)]
        change = True
        while change:
            change = False
            for i in range(lignes):
                for j in range(colonnes):
                    if niveaux_energie[i][j] > 9 and not clignotant[i][j]:
                        clignotant[i][j] = True
                        change = True
                        clignote += 1
                        # Augmenter le niveau d’énergie des octopus adjacents de 1
                        for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
                            if 0 <= r < lignes and 0 <= c < colonnes:
                                niveaux_energie[r][c] += 1
        #Réinitialiser le niveau d’énergie des octopus qui clignote à 0
        niveaux_energie = [[0 if f else e for f, e in zip(flash_row, energy_row)] for flash_row, energy_row in zip(clignotant, niveaux_energie)]
    return clignote
def main(args):
    resultat = simuler_etapes(args.niveaux_energie, args.etapes)
    print(resultat)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simule le nombre d'étapes données en comptant le nombre d'octopus qui clignotent.")
    parser.add_argument("niveaux_energie", help="une matrice d'entiers représentant les niveaux d'énergie des octopus", type=eval)
    parser.add_argument("etapes", help="un entier représentant le nombre d'étapes à simuler", type=int)
    args = parser.parse_args()
    main(args)