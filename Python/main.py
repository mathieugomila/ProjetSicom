import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import math 

N = 100

def obtenirCourbeChiffre1():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    
    x[0:N//3] = np.linspace(0.25, 0.5, N//3)
    y[0:N//3] = np.linspace(0.6, 0.90, N//3)
    
    x[N//3:] = 0.5
    y[N//3:] = np.linspace(0.90, 0.1, N - N//3)
    
    
    return x,y,z

def obtenirCourbeChiffre2():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    
    a = np.linspace(0, np.pi, N//2)
    
    x[0:N//2] = 0.5 + 0.25 * np.cos(np.pi - a)
    y[0:N//2] = 0.6 + 0.25 * np.sin(np.pi - a)
    
    x[N//2: 3 * N//4] = np.linspace(0.75, 0.25, 3 * N//4 - N//2)
    y[N//2: 3 * N//4] = np.linspace(0.6, 0.1, 3 * N//4 - N//2)
    
    x[3 * N//4:] = np.linspace(0.25, 0.75, N - 3 * N//4)
    y[3 * N//4:] = 0.1
    
    return x,y,z

def obtenirCourbeChiffre3():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    
    a = np.linspace(0, 1.5 * np.pi, N//2)
    
    x[0:N//2] = 0.5 + 0.20 * np.cos(np.pi - a)
    y[0:N//2] = 0.7 + 0.2 * np.sin(np.pi - a)
    
    x[N//2:] = 0.5 + 0.20 * np.cos(np.pi/2 - a)
    y[N//2:] = 0.3 + 0.2 * np.sin(np.pi/2 - a) 
    
    
    return x,y,z

def obtenirCourbeChiffre4():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    
    x[0:N//3] = 0.5
    y[0:N//3] = np.linspace(0.1, 0.9, N//3)
    
    x[N//3: 2 * N//3] = np.linspace(0.5, 0.2, 2 * N//3 - N//3)
    y[N//3: 2 * N//3] = np.linspace(0.9, 0.35, 2 * N//3 - N//3)
    
    x[2 * N//3:] = np.linspace(0.2, 0.65, N - 2 * N//3)
    y[2 * N//3:] = 0.35
    
    return x,y,z

def obtenirCourbeChiffre5():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    
    a = np.linspace(0, np.pi, N//2)
    
    x[0:N//2] = 0.4 + 0.25 * np.sin(np.pi - a)
    y[0:N//2] = 0.3 + 0.2 * np.cos(np.pi - a)
    
    x[N//2:3*N//4] = 0.4
    y[N//2:3*N//4] = np.linspace(0.5, 0.8, N//4)
    
    
    x[3*N//4:] = np.linspace(0.4, 0.65, N//4)
    y[3*N//4:] = 0.8
    
    return x,y,z


def obtenirCourbeChiffre6():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    
    a = np.linspace(0.5 * np.pi, 3 * np.pi, N)
    b = np.linspace(0.6, 0.5, N//5)
    
    x[0:N//5] = 0.5 + 0.25 * np.cos(a[0:N//5])
    x[N//5:] = 0.5 + 0.25 * np.cos(a[N//5:])
    y[0:N//5] = 0.3 + b * np.sin(a[0:N//5])    
    y[N//5:] = 0.3 + 0.2 * np.sin(a[N//5:])
    
    return x,y,z

#La variable z gère les levers de stylos de la machine
def obtenirCourbeChiffre7():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    
    x[:N//4] = np.linspace(0.45, 0.65, N//4)
    y[:N//4] = 0.5
    z[:N//4] = 1
    
    x[N//4:N//2] = np.linspace(0.65, 0.45, N//4)
    y[N//4:N//2] = np.linspace(0.5, 0.2, N//4)
    z[N//4:N//2] = 0

    x[N//2:3*N//4] = np.linspace(0.45, 0.65, N//4)
    y[N//2:3*N//4] = np.linspace(0.2, 0.8, N//4)
    z[N//2:3*N//4] = 1
    

    
    x[3*N//4:] = np.linspace(0.65, 0.35, N//4)
    y[3*N//4:] = 0.8
    z[3*N//4:] = 1
    
    return x,y,z


def obtenirCourbeChiffre8():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    z[0:N//24] = 0
    
    a = np.linspace(0, 2 * np.pi, N//2)
    
    x[0:N//2] = 0.5 + 0.2 * np.cos(np.pi/2 - a)
    y[0:N//2] = 0.3 + 0.2 * np.sin(np.pi/2 - a)

    x[N//2:] = 0.5 + 0.17 * np.cos(-np.pi/2 + a)
    y[N//2:] = 0.67 + 0.17 * np.sin(-np.pi/2 + a)
    
    return x,y,z

def obtenirCourbeChiffre9():
    x = np.ndarray(N)
    y = np.ndarray(N)
    z = np.ones(N, dtype='float64')
    z[0:N//24] = 0
    
    a = np.linspace(0.5 * np.pi, 3 * np.pi, N)
    b = np.linspace(0.6, 0.5, N//5)
    
    x[0:N//5] = 1 - (0.5 + 0.25 * np.cos(a[0:N//5]))
    x[N//5:] = 1 - (0.5 + 0.25 * np.cos(a[N//5:]))
    y[0:N//5] = 1 - (0.3 + b * np.sin(a[0:N//5]))    
    y[N//5:] = 1 - (0.3 + 0.2 * np.sin(a[N//5:]))
    
    return x,y,z

def obtenirCourbeChiffre(n):
    if(n == 1):
        return obtenirCourbeChiffre1()
    if(n == 2):
        return obtenirCourbeChiffre2()
    if(n == 3):
        return obtenirCourbeChiffre3()
    if(n == 4):
        return obtenirCourbeChiffre4()
    if(n == 5):
        return obtenirCourbeChiffre5()
    if(n == 6):
        return obtenirCourbeChiffre6()
    if(n == 7):
        return obtenirCourbeChiffre7()
    if(n == 8):
        return obtenirCourbeChiffre8()
    if(n == 9):
        return obtenirCourbeChiffre9()

def rotationPoint(x, y, angle):
    distance_centre = math.sqrt((x-0.5)**2 + (y-0.5)**2)
    argument = 0
    if(y == 0.5 and x < 0.5): # réel négatif
        argument = np.pi
    elif (x - 0.5 + distance_centre == 0) :
        x = 0.5
        y = 0.5
        return x, y
        
    else :
        argument = 2 * math.atan((y - 0.5)/(x - 0.5 + distance_centre))
    x = distance_centre * math.cos(argument + angle) + 0.5
    y = distance_centre * math.sin(argument + angle) + 0.5
    
    return x,y
    

def rotationChiffre(courbe, angle):
    x_origine, y_origine = courbe[0], courbe[1]
    x_rotation, y_rotation = np.ndarray(N), np.ndarray(N)
    
    z=courbe[2]
    
    for i in range(0, N):
        x_rotation[i], y_rotation[i] = rotationPoint(x_origine[i], y_origine[i], angle) 
    return x_rotation, y_rotation, z

def modifierValeur(i, j, valeur, grille):
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

    #tant que la grille n'est pas correcte
    while(verifierGrille(grilleResolution) == False) : 
        #antiBoucleInfini = antiBoucleInfini + 1
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
    #print("Resolution en " + str(antiBoucleInfini) + " itérations")
    print("Resolution en " + str((temps_fin - temps_debut)*1000) + "ms")
    return grilleResolution 
    


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

import serial  # Importing the serial library to communicate with Arduino
from time import sleep # Importing the time library to provide the delays in program

# Defined the port and the baudrate at which we will communicate with Arduino.
# It should be same on the Arduino side.
# If you don't know the port at which Arduino is connected. Read the step 2 of the first example.
# ser = serial.Serial('/dev/ttyACM0', 115200) 
# for k in range(1,10):
#     x, y, z = rotationChiffre(obtenirCourbeChiffre(k), k)
#     
#     
# 
#     for i in range(0, N + 10):
#         sleep(0.020)
#         if(i < 10):
#             valeur = [str(int(x[0] * 200 + 200 * k)), str(int(y[0]*200)), str(int(0))]  
#         else :# Convert the integers to a comma-separated string
#             valeur = [str(int(x[i - 10] * 200 + 200 * k)), str(int(y[i - 10]*200)), str(int(z[i - 10]))]    
#         send_string = ','.join(valeur)
#         send_string += "\n"
# 
#         # Send the string. Make sure you encode it before you send it to the Arduino.
#         ser.write(send_string.encode('utf-8'))
    #sleep(0.020)
    #valeur = [str(int(x[N-1] * 200 + 200 * k)), str(int(y[N-1]*200)), str(int(0))]    
    #send_string = ','.join(valeur)
    #send_string += "\n"

    # Send the string. Make sure you encode it before you send it to the Arduino.
    #ser.write(send_string.encode('utf-8'))
    #sleep(0.5)    

racine_taille = 3
taille = racine_taille ** 2


def tracerCarre(x, y, taille):
    x_carre = [x - taille, x + taille, x + taille, x - taille, x - taille]
    y_carre = [y + taille, y + taille, y - taille, y - taille, y + taille]
    return x_carre, y_carre


def tracerChiffreSurGrille(i, j, valeur):
    longueur_case_x = 2000/taille
    longueur_case_y = 2000/taille
    
    if(valeur == 0):        
        return
    
    x, y, z = obtenirCourbeChiffre(valeur)
    x = x * longueur_case_x + longueur_case_x * j + 500
    y = y * longueur_case_y + 500 + (longueur_case_y * (taille - 1)) - longueur_case_y * i
    
    
    return x, y, z

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


grille =[[0 for i in range(0,taille)] for j in range(0,taille)]
creerGrilleSimple1(grille)
affichageGrille(grille)
#grille = resolutionGrille(grille)
ser = serial.Serial('/dev/ttyACM0', 115200)

for i in range(0, taille):
    for j in range(0, taille):
        print(grille[i][j])
        
        #x, y = tracerCarre(1500,1500,1000)
        if(grille[i][j] != 0):
            x, y, z = tracerChiffreSurGrille(i, j, grille[i][j])
            for k in range(0, N + 10):
                sleep(0.02)
                if(k < 10):
                    valeur = [str(int(x[0])), str(int(y[0])), str(int(0))]  
                else :# Convert the integers to a comma-separated string
                   valeur = [str(int(x[k - 10])), str(int(y[k - 10])), str(int(z[k-10]))]    
                send_string = ','.join(valeur)
                send_string += "\n"

                # Send the string. Make sure you encode it before you send it to the Arduino.
                ser.write(send_string.encode('utf-8'))

