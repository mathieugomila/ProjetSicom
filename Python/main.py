import rognage
import resolution
import ecriture

#### 1) Récupérer l'image et rogner les bords de l'image ####
img_rognee = rognage.photo_rognage('Image')

# Recupérer les coordonnées x et y des 4 bords de la grille
#xOffset, yOffset, tailleCase, angle  = traitementImage.recupererBord(img_rognee)

#### 2) Détecter les chiffres présents sur la grille ####
#grille = traitementImage.detecterChiffres(img_rognee, xOffset, yOffset)

#### 3) Résoudre la grille ####
#grilleSansChiffreOrigine = resolutionGrilleSansChiffreOrigine(grille)


#### 4) Commander l'écriture de la grille ####
#tracerSolutionSurGrille(grilleSansChiffreOrigine, offsetX, offsetY, tailleCase, angle)