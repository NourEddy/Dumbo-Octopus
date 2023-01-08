# Dumbo-Octopus
Cet exercice simule le comportement d'un groupe d'Octopus en augmentant leur niveau d'énergie au fil des étapes de la simulation. Si un octopode a un niveau d'énergie supérieur à 9, il clignote et augmente le niveau d'énergie de ses Octopus adjacents de 1. Les Octopus qui clignotent réinitialisent leur niveau d'énergie à 0.  
### Utilisation  
Le programme prend en entrée une matrice de niveaux d'énergie des Octopus au début de la simulation et un entier indiquant le nombre d'étapes de la simulation. cet exercice de divise en deux phases, la première phase permet d'affichera le nombre total d'octopus qui ont clignoté pendant le nombre d'étapes définie pour la simulation. la deuxième phase permet d'afficher un message indiquant à quelle étape tous les Octopus ont clignoté simultanément, ou un message indiquant que tous les Octopus n'ont pas clignoté simultanément pendant la simulation.  
Voici comment exécuter le programme de la première phase avec des arguments de test :  
`python octopus_flash.py "[[4,3,4,1,3,4,7,6,4,3],[5,4,7,7,7,2,8,4,5,1],[2,3,2,2,7,3,3,8,7,8],[5,4,5,3,7,6,2,5,5,6],[2,7,1,8,1,2,3,4,2,1],[4,2,3,7,8,8,6,1,1,5],[5,6,3,1,6,1,7,1,1,4],[2,2,1,7,6,6,7,2,2,7],[4,2,3,6,5,8,1,2,5,5],[4,4,8,2,6,2,7,6,4,1]]" 100  `  
Le script compte le nombre total d'octopus qui ont clignoté pendant toutes les étapes de la simulation et affiche ce nombre à la fin.  
Pour la deuxième phase on change seulement le nom de la fonction en mettant  
`python all_octopus_flash.py "[[4,3,4,1,3,4,7,6,4,3],[5,4,7,7,7,2,8,4,5,1],[2,3,2,2,7,3,3,8,7,8],[5,4,5,3,7,6,2,5,5,6],[2,7,1,8,1,2,3,4,2,1],[4,2,3,7,8,8,6,1,1,5],[5,6,3,1,6,1,7,1,1,4],[2,2,1,7,6,6,7,2,2,7],[4,2,3,6,5,8,1,2,5,5],[4,4,8,2,6,2,7,6,4,1]]" 400  `  

 ` 
