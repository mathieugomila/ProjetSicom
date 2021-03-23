from math import sqrt
import time

racine_taille = 3
taille = racine_taille ** 2

#grille = [[0 for i in range(0,taille)] for j in range(0,taille)]

def creationGrilleVide():
    return [[0 for i in range(0,taille)] for j in range(0,taille)]


def modifierValeur(i, j, valeur, grille):
    """i = numéro ligne (0 à 9), j = numéro colonne (0 à 9) et valeur de 0 à 9(inclus et avec 0 pour case vide)"""
    if(valeur > taille):
        return False
    grille[i][j] = valeur
    
def verifierLigne(i, grille):
    presence = [0 for j in range(0, taille)]
    for j in range(0, taille):
        if(grille[i][j] != 0 and presence[grille[i][j] - 1] == 1):
            return False
        if(grille[i][j] != 0):
            presence[grille[i][j]- 1] = presence[grille[i][j] - 1] + 1
    return True  
        

def verifierColonne(j, grille):
    presence = [0 for i in range(0, taille)]
    for i in range(0, taille):
        if(grille[i][j] != 0 and presence[grille[i][j] - 1] == 1):
            return False
        if(grille[i][j] != 0):
            presence[grille[i][j]- 1] = presence[grille[i][j] - 1] + 1
    return True  

def verifierBloc(i, j, grille):
    presence = [0 for j in range(0, taille)]
    for x in range(i//racine_taille * racine_taille, (i//racine_taille) * racine_taille + racine_taille):
        for y in range(j//racine_taille * racine_taille, (j//racine_taille) * racine_taille + racine_taille):
            if(grille[x][y] != 0 and presence[grille[x][y] - 1] == 1):
                return False
            if(grille[x][y] != 0):
                presence[grille[x][y] - 1] = presence[grille[x][y] - 1] + 1
    return True
            
            
def verifierValeur(i, j, grille):
    if(verifierLigne(i, grille) and verifierColonne(j, grille) and verifierBloc(i, j, grille)):
        return True
    return False

def verifierGrille(grille):
    for i in range(0, taille):
        for j in range(0, taille):
            if(grille[i][j] == 0 or verifierValeur(i, j, grille) == False):
                return False
    return True

def trouverChiffresPossibles(i, j, grille):
    possibilite = []
    for k in range(1, taille + 1):
        modifierValeur(i, j, k, grille)
        if(verifierValeur(i, j, grille)):
            possibilite.append(k)
    modifierValeur(i, j, 0, grille)
    return possibilite               



def trouverNumerosPossibles(grille):
    grilleNumerosPossibles = [[[] for i in range(0,taille)] for j in range(0,taille)]
    for i in range(0, taille):
        for j in range(0, taille):
            if(grille[i][j] == 0):
                grilleNumerosPossibles[i][j] = trouverChiffresPossibles(i, j, grille)
    return grilleNumerosPossibles

def compterNombreNumerosPossibles(grille):
    nouvelleGrille = trouverNumerosPossibles(grille)
    grilleComptage = [[0 for i in range(0,taille)] for j in range(0,taille)]
    for i in range(0, taille):
        for j in range(0, taille):
            grilleComptage[i][j] = len(nouvelleGrille[i][j])
    return grilleComptage

def trouverOrdreRemplissage(grilleComptage):
    ordreGrille = [[0 for i in range(0,taille)] for j in range(0,taille)]
    ordre = 1
    for k in range(1, taille + 1):
        for i in range(0, taille):
            for j in range(0, taille):
                if(grilleComptage[i][j] == k):
                    ordreGrille[i][j] = ordre
                    ordre = ordre + 1
    return ordreGrille

def trouverNumeroAuDessus(grille, grilleNumerosPossibles, i, j):
    valeur = grille[i][j]
    liste = grilleNumerosPossibles[i][j]
    
    if(valeur == 0 and len(liste) > 0):
        return liste[0]
    if(valeur == 0 and len(liste) == 0):
        return -1
    
    for i in range(0, len(liste)) : 
        if(valeur == liste[i]):
            if(i == len(liste) - 1):
                return -1
            return liste[i+1]
    return -1

def trouverPositionIndicePointeur(ordreGrille, indicePointer):
    for i in range(0, taille):
        for j in range(0, taille):
            if(ordreGrille[i][j] == indicePointer):
                return i,j
    print("Ne trouve pas " + str(indicePointer))
    return -1,-1
    
    

def resolutionGrille(grille):
    # ordre de remplisage des cases vides :
    temps_debut = time.time()   
        
        
    ordreGrille = [[0 for i in range(0,taille)] for j in range(0,taille)]
    ordreGrille = trouverOrdreRemplissage(compterNombreNumerosPossibles(grille))
    
    # les numéros qui peuvent être présent sur les cases :
    grilleNumerosPossibles = trouverNumerosPossibles(grille)    
    
    # grille qui sera en sorti de l'algorithme
    grilleResolution = [[grille[i][j] for j in range(0,taille)] for i in range(0,taille)] #copie grille
    #affichageGrille(grilleResolution)
    indicePointeur = 1 #indice de la case à modifier
    antiBoucleInfini = 0
    #tant que la grille n'est pas correcte
    while(verifierGrille(grilleResolution) == False and antiBoucleInfini < 1000000) : 
        antiBoucleInfini = antiBoucleInfini + 1
        #trouver position pour indice Pointer
        #print("On cherche la case dont l'indice pointeur est " + str(indicePointeur))
        i,j = trouverPositionIndicePointeur(ordreGrille, indicePointeur)
        #print("Modification de la case " + str(i) + ";" + str(j))
        if(i == -1):
            print("   [BUG] indice non correcte")
        # SI le nombre est 0 (case vide) :
        nouvelleValeur = trouverNumeroAuDessus(grilleResolution, grilleNumerosPossibles, i, j)
        #print("   Nouvelle valeur potentielle : " + str(nouvelleValeur))
        if(nouvelleValeur == -1):
            #print("   Pas de valeurs possibles")
            modifierValeur(i, j, 0, grilleResolution)
            indicePointeur = indicePointeur - 1
        else :
            modifierValeur(i, j, nouvelleValeur, grilleResolution)
            #affichageGrille(grilleResolution)
            if(verifierValeur(i, j, grilleResolution)):
                indicePointeur = indicePointeur + 1
                #print("   La grille est bonne, on continue")
    temps_fin = time.time()        
    print("Resolution en " + str(antiBoucleInfini) + " itérations")
    print("Resolution en " + str((temps_fin - temps_debut)*1000) + "ms")
    return grilleResolution 
    
def resolutionGrilleSansChiffreOrigine(grille):
    grilleSansChiffreOrigine = [[0 for i in range(0,taille)] for j in range(0,taille)]
    grilleResolution = resolutionGrille(grille)
    for i in range(0, taille):
        for j in range(0, taille):
            grilleSansChiffreOrigine[i][j] = grilleResolution[i][j] - grille[i][j]
    return grilleSansChiffreOrigine

def affichageGrille(grille):
    ligneTrait = "-------------"
    colonneTrait = "|"

    for i in range(0, taille):
        if(i%racine_taille == 0):
            print(ligneTrait)
        ligne = ""
        ligne = ligne + colonneTrait   
        for j in range(0, taille):
            if(grille[i][j] != 0):
                ligne = ligne + str(grille[i][j])
            else : 
                ligne = ligne + "-"
            if(j%racine_taille == racine_taille - 1):
                ligne = ligne + colonneTrait
        print(ligne)   
    print(ligneTrait)           

def creerGrilleSimple1(grille):    
    modifierValeur(0, 0, 5, grille)
    modifierValeur(0, 1, 3, grille)
    modifierValeur(0, 4, 7, grille)
    modifierValeur(1, 0, 6, grille)
    modifierValeur(1, 3, 1, grille)
    modifierValeur(1, 4, 9, grille)
    modifierValeur(1, 5, 5, grille)
    modifierValeur(2, 1, 9, grille)
    modifierValeur(2, 2, 8, grille)
    modifierValeur(2, 7, 6, grille)
    
    modifierValeur(3, 0, 8, grille)
    modifierValeur(3, 4, 6, grille)
    modifierValeur(3, 8, 3, grille)
    modifierValeur(4, 0, 4, grille)
    modifierValeur(4, 3, 8, grille)
    modifierValeur(4, 5, 3, grille)
    modifierValeur(4, 8, 1, grille)
    modifierValeur(5, 0, 7, grille)
    modifierValeur(5, 4, 2, grille)
    modifierValeur(5, 8, 6, grille)
    
    modifierValeur(6, 1, 6, grille)
    modifierValeur(6, 6, 2, grille)
    modifierValeur(6, 7, 8, grille)
    modifierValeur(7, 3, 4, grille)
    modifierValeur(7, 4, 1, grille)
    modifierValeur(7, 5, 9, grille)
    modifierValeur(7, 8, 5, grille)
    modifierValeur(8, 4, 8, grille)
    modifierValeur(8, 7, 7, grille)
    modifierValeur(8, 8, 9, grille)

def creerGrilleTresDifficile1(grille):

    modifierValeur(0, 0, 8, grille)
    modifierValeur(1, 2, 3, grille)
    modifierValeur(1, 3, 6, grille)
    modifierValeur(2, 1, 7, grille)
    modifierValeur(2, 4, 9, grille)
    modifierValeur(2, 6, 2, grille)
    
    modifierValeur(3, 1, 5, grille)
    modifierValeur(3, 5, 7, grille)
    modifierValeur(4, 4, 4, grille)
    modifierValeur(4, 5, 5, grille)
    modifierValeur(4, 6, 7, grille)
    modifierValeur(5, 3, 1, grille)
    modifierValeur(5, 7, 3, grille)
    
    modifierValeur(6, 2, 1, grille)
    modifierValeur(6, 7, 6, grille)
    modifierValeur(6, 8, 8, grille)
    modifierValeur(7, 2, 8, grille)
    modifierValeur(7, 3, 5, grille)
    modifierValeur(7, 7, 1, grille)
    modifierValeur(8, 1, 9, grille)
    modifierValeur(8, 6, 4, grille)                
                