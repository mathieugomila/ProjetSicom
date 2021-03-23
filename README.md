# Interfaces entre les différents fichiers

## Création de la grille : 

Pour créer une grille vide de taille 9x9: 

'''
grille = creationGrilleVide()
'''

-----------

Pour remplir la i-ème ligne et j-ième colonne (en commençant à l'indice 0) avec la valeur v: 

'''
modifierValeur(i, j, v, grille)
'''

## Résolution de la grille : 

Une fois la grille complétée, pour obtenir la grille des valeurs à écrire (donc la grille finale sans les valeurs d'origines) : 

'''
resolutionGrilleSansChiffreOrigine(grille)
'''

Cette fonction retourne une grille sur laquelle les 0 correspondent aux cases sur lesquelles il ne faut pas écrire (sur lesquelles il y a les valeurs de base).


