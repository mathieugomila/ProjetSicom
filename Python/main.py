import rognage
import resolution
import ecriture


#### 1) Récupérer l'image et rogner les bords de l'image ####
img_rognee = rognage.photo_rognage('')

import traitementImage

# Recupérer les coordonnées x et y des 4 bords de la grille et la grille résolue
grille, angle, xsg, xsd, xid, xig, ysg, ysd, yid, yig  = traitementImage.main(img_rognee)
offsetX = xig
offsetY = yig
tailleCase = (xsd - xsg) /9

#### 3) Résoudre la grille ####
grilleSansChiffreOrigine = resolution.resolutionGrilleSansChiffreOrigine(grille)


#### 4) Commander l'écriture de la grille ####
ecriture.tracerSolutionSurGrille(grilleSansChiffreOrigine, offsetX, offsetY, tailleCase, angle)