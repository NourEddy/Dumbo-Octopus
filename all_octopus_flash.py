# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 21:57:07 2023

@author: Nour Eddine
"""
import argparse
def simuler_etapes(niveaux_energie, etapes):
    lignes = len(niveaux_energie)
    colonnes = len(niveaux_energie[0])
    # Initialise une liste vide pour stocker l'historique des niveaux d'énergie
    historique_energie = []
    for etapee in range(etapes):
        historique_energie.append(niveaux_energie)
        # Augmenter le niveau d’énergie de chaque octopus de 1
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
                        # Augmenter le niveau d’énergie des octopus adjacents de 1
                        for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
                            if 0 <= r < lignes and 0 <= c < colonnes:
                                niveaux_energie[r][c] += 1
        # Réinitialiser le niveau d’énergie des octopus qui clignote à 0
        niveaux_energie = [[0 if f else e for f, e in zip(flash_row, energy_row)] for flash_row, energy_row in zip(clignotant, niveaux_energie)]
    return historique_energie
def main(args):
    # Récupérer les valeurs des arguments
    niveaux_energie = args.niveaux_energie
    etapes = args.etapes
    historique_energie = simuler_etapes(niveaux_energie, etapes)
    for etape, niveaux_energie in enumerate(historique_energie):
        tous_clignote = True
        for i in range(len(niveaux_energie)):
            for j in range(len(niveaux_energie[0])):
                if niveaux_energie[i][j] != 0:
                    tous_clignote = False
                    break
            if not tous_clignote:
                break
        if tous_clignote:
            print(f"Tout les octopus ont clignoté à l'etape {etape}.")
            break
    else:
        print('Tout les octopus n’ont pas clignoté simultanément pendant la simulation.')
if __name__ == '__main__':
    # Créer un parseur d'arguments
    parser = argparse.ArgumentParser(description="découvrir à quelle étape tous les octopus s'allume en même temps.")
    # Ajouter un argument pour les niveaux d'énergie sous la forme d'une matrice
    parser.add_argument('niveaux_energie',  help="Les niveaux d'énergie de chaque octopus au début de la simulation.", type=eval )
    # Ajouter un argument pour le nombre d'étapes de la simulation
    parser.add_argument('etapes', help="Le nombre d'étapes de la simulation.", type=int)
    args = parser.parse_args()
    main(args)