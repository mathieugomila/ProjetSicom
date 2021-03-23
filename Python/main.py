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
    """tourne le point de coordonnées (x,y) compris dans [0; 1] d'un certain angle (radient)"""
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


def obtenirCourbeChiffreAvecAngle(valeur, angle, tailleChiffre):
    if(valeur == 0):        
        return
    
    x, y, z = rotationChiffre(obtenirCourbeChiffre(valeur), angle)
    x = x * tailleChiffre 
    y = y * tailleChiffre
    
    
    return x, y, z


def tracerSolutionSurGrille(grilleSansChiffreOrigine, offsetX, offsetY, tailleCase,  angle):
    ser = serial.Serial('/dev/ttyACM0', 115200)
    
    chiffres = [obtenirCourbeChiffreAvecAngle(v, angle, tailleCase) for v in range(1, 10)]

    for i in range(0, taille):
        for j in range(0, taille):
            print(grilleSansChiffreOrigine[i][j])
            
            #x, y = tracerCarre(1500,1500,1000)
            if(grilleSansChiffreOrigine[i][j] != 0):
                x, y, z = chiffres[grilleSansChiffreOrigine[i][j] - 1]
                offsetXCase = offsetX + math.cos(angle + math.pi/2) * tailleCase * (8 - i)
                offsetYCase = offsetY + math.sin(angle + math.pi/2) * tailleCase * (8 - j)
                for k in range(0, N + 10):
                    sleep(0.02)
                   
                    if(k < 10):
                        valeur = [str(int(x[0] + offsetXCase)), str(int(y[0] + offsetYCase)), str(int(0))]  
                    else :# Convert the integers to a comma-separated string
                        valeur = [str(int(x[k - 10] + offsetXCase)), str(int(y[k - 10] + offsetYCase)), str(int(z[k-10]))]    
                    send_string = ','.join(valeur)
                    send_string += "\n"

                    # Send the string. Make sure you encode it before you send it to the Arduino.
                    ser.write(send_string.encode('utf-8'))

