# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:12:54 2021

@author: cmbbd
"""


from __future__ import print_function
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import numpy as np
import cv2
from skimage import color
from os.path import join
import skimage.io as skio
import skimage as sk
import matplotlib.pyplot as plt
import csv
from sklearn.model_selection import train_test_split
import skimage.util as sku
from scipy.signal import convolve2d
plt.rcParams['image.cmap'] = 'gray'
plt.close('all')


#Charger les images d'entrainement et de tests à partir d'un fichier excel
nb_base=8
nb_pixel_im=28*28
file = open('names.csv',"r")
data = csv.reader(file, delimiter = ";")
dat = np.array(list(data))
X= np.zeros((len(dat),nb_pixel_im),int)
for i in range(len(dat)):
        for j in range(nb_pixel_im):
            X[i,j] = float(dat[i,j])

#Séparer la base de donnée d'image en base trai et test
(trainData1, testData, trainLabels1, testLabels) = train_test_split(X,
	[k//nb_base+1 for k in range(0,nb_base*9)], test_size=0.01, random_state=9)
def index(TAB,i):
    for j in range(len(TAB)):
        if (TAB[j]==i):
            return(j)

#Noyau de la convolution 2D
kernel = np.ones((3,3),np.uint8)


#Nombre d'images pour chaque digit dans la base de donnée inférieur ou égal à 9
sizetrain = nb_base

#Taille de la base de donnée test
sizetest = len(testLabels)
#K choisi pour le modèle KNN
K=[]
ACC = []
SEUIL = []

#Boucle pour évaluer le meilleur couple k et seuil
for k in range (4,5):
   for seuil in range(6,7):
    K.append(k)
    
    #Seuil choisis pour binariser les image de la base de donnée
    seuil = seuil/10
    SEUIL.append(seuil)
    ### Liste contenant les prédictions
    RESULT = []
    NBDIGIT = [[]for i in range(sizetest)]
    
    # Dans le cas où on teste différents paramètres contient les k et seuils testés
    KJ = []
    
    
    #Liste contenant la rapport de classification
    REPORT = []
    
    
    #Liste contenant la précision du modèle pour un test donné
    ACCURACY = []
    
    #Liste contenant le digit apparaissant le plus pour chaque colonne de RESULT
    FREQUENCE = []
    #Listes contenant les images test (BINKS) et d'entraînement (TRAIN)
    
    IMGtest = []
    IMGtrain = []
    
    
        
    
    def accurate(L,M):
        Faux = []
        U = (np.array(L)==np.array(M))
        for i in range(len(U)) :
            if not(U[i]):
                Faux.append(i)
                
        return(np.sum(U)/len(U),Faux)
    def plusfreq(LISTE):
        #Retourne la valeur la plus fréquente de LISTE
        FREQ = []
        COMPT = []
        for i in range(len(LISTE)):
            if (LISTE[i] not in COMPT):
                COMPT.append(LISTE[i])
                FREQ.append(1)
            else:
                FREQ[COMPT.index(LISTE[i])]+=1
        return(COMPT[(np.argmax(FREQ))])
                
                
    def trainsplit(trindat,labels,digit1,digit2):
        LabelsDG1 = []
        LabelsDG2 = []
        for i in range(len(labels)):
            if (labels[i]==digit1):
                LabelsDG1.append(i)
            if (labels[i]==digit2):
                LabelsDG2.append(i)            
        TEMP = []
        for i in range(len(LabelsDG1)):
            TEMP.append(trindat[LabelsDG1[i]])
        for i in range(len(LabelsDG2)):
            TEMP.append(trindat[LabelsDG2[i]])
        return([TEMP,[digit1 for i in range(len(LabelsDG1))]+[digit2 for i in range(len(LabelsDG2))]])
    
    def precision(traindata,stop,TEST,DIGIT):
        for i in range(len(DIGIT)-1):
            if (i==0):
                digit1=DIGIT[i]
                digit2 = DIGIT[i+1]
            else:
                
                digit1=plusfreq(RESULT)
                digit2 = DIGIT[i+1]
                
            #print((digit1,digit2))            
            traindata2= trainsplit(traindata, trainLabels1, digit1, digit2)
            #print(traindata2)
            RESULT =[]
            labels = traindata2[1]
            for k in range(1,stop):
                model = KNeighborsClassifier(n_neighbors=k)
                model.fit(traindata2[0],traindata2[1])
                prediction = model.predict(TEST)
                RESULT.append(prediction[0])
        return([plusfreq(RESULT),RESULT])
    
    def affiche_image(image,titre='test'):
        plt.figure()
        plt.imshow(image), plt.title(titre)
    
    def pourcentage_blanc(image):
        L,C=np.shape(image)
        compt=0
        nb_pixel=L*C
        for i in range (L):
            for j in range (C):
                if image[i,j]==255:
                    compt+=1
        return (compt/nb_pixel)
    
    def mange_ligne(image):
        L,C=np.shape(image)
        truc_a_manger=np.zeros((L,C))
        for j in range (C):
            i=0
            truc_a_manger[i,j]=1
            while i+1<L and image[i+1,j]==0 :
                truc_a_manger[i+1,j]=1
                i+=1
        for j in range(C):
            i=L-1
            truc_a_manger[i,j]=1
            while i-1>0 and image[i-1,j]==0 :
                truc_a_manger[i-1,j]=1
                i-=1
        for i in range (L):
            j=0
            truc_a_manger[i,j]=1
            while j+1<C and image[i,j+1]==0 :
                truc_a_manger[i,j+1]=1
                j+=1
        for i in range(L):
            j=C-1
            truc_a_manger[i,j]=1
            while j-1>0 and image[i,j-1]==0 :
                truc_a_manger[i,j-1]=1
                j-=1
        for i in range(L):
            for j in range(C):
                if truc_a_manger[i,j]==1:
                    image[i,j]=255
        return image
                
                
    #image doit être en niveau de gris sur des ubytes
    def extrait_chiffre(image,seuil_aire,seuil_bas):
        ret, thresh = cv2.threshold(image, seuil_bas, 255, cv2.THRESH_BINARY_INV)
        #affiche_image(thresh,'thresh')
        thresh = sku.invert(thresh)
        thresh = mange_ligne(thresh)
        thresh = sku.invert(thresh)
    
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        roi=np.zeros((2,2))
        for cnt in contours:
            # on vérifie la taille du contour pour éviter de traiter un 'défaut'
            i=cv2.contourArea(cnt)
            if cv2.contourArea(cnt) > seuil_aire:
                # on récupère le rectangle encadrant le chiffre
                brect = cv2.boundingRect(cnt)
                x,y,w,h = brect
                # extraction de notre "region of interest"
                # notre roi correspond à un chiffre sur notre feuille
                roi_nv = thresh[y:y+h, x:x+w]
                if pourcentage_blanc(roi_nv)>pourcentage_blanc(roi):
                    roi=roi_nv
        #affiche_image(roi,'roi'+str(i))
        return roi
    
    
    #Permet de predir le label de l'immage en entrée à partir de model
    def test(filename , dirpath, model):
        filepath = join(dirpath, filename)
        imgi = skio.imread(filepath)
        imgi = color.rgb2gray(imgi)
        imgi = sku.invert(imgi)
        #plt.figure()
        #plt.imshow(imgi)
        imgi = sk.img_as_ubyte(imgi)
        binks = imgi
        binks = cv2.resize(binks,(28,28))
        binks = sk.img_as_ubyte(binks)
        binks = (binks > (seuil * np.max(binks)))*1
        binks = sk.img_as_ubyte(binks)
        image = binks
        predic = model.predict(image.reshape(1,-1))
        #plt.figure()
        #plt.imshow(image)
        return(predic[0])
    #Boucles pour évaluer les différents paramètres
    
                
                
    #Listes contenant les images test (TEST) et d'entraînement (DIGITS) après modifications et en ligne
    DIGITS = []
    TEST = []
    
    
     
    #Boucle permettant le chargement et le traitement des images tests
    for y in range(len(testLabels)):
        #On charge une image test que l'on met en 28x28
        imgi = color.rgb2gray(testData[y].reshape(28,28))
        imgi = sku.invert(imgi)
        #On extrait l'objet (le chiffre) de l'image
        imgi = extrait_chiffre(sk.img_as_ubyte(imgi),20,128)
        binks = imgi
        #On resize l'image obtenue en 28x28
        binks = cv2.resize(binks,(28,28))
        #binks = sku.invert(binks)
        binks = sk.img_as_ubyte(binks)
        #On binarise l'image
        #binks = (binks > (seuil * np.max(binks)))*1
        binks = sk.img_as_ubyte(binks)
        image = binks
        IMGtest.append(image)
        #image = cv2.erode(image,kernel2)
        
        (TEST.append(image.reshape(1, -1)[0]))
    
     
    #Boucles permettant le chargement et le traitement des images trains
    for p  in range(0,len(trainLabels1)):
        #On charge une image test que l'on met en 28x28
        imgi = color.rgb2gray(trainData1[p].reshape(28,28))
        #imgi = sku.invert(imgi)
        #On extrait l'objet (le chiffre) de l'image
        imgi = extrait_chiffre(sk.img_as_ubyte(imgi),0,128)
        binks = imgi
        #On resize l'image obtenue en 28x28
        binks = cv2.resize(binks,(28,28))
        binks = sk.img_as_ubyte(binks)
        #On binarise l'image
        binks = (binks > (seuil * np.max(binks)))*1
        binks = sk.img_as_ubyte(binks)
        image = binks
        #On filtre l'image (filtre médian)
        image = convolve2d(binks,[[1/9 for j in range(3)]for i in range(3)],fillvalue=0)
        image = (image > (0.1* np.max(image)))*1
        image = image.astype('uint8')
        #On resize l'image obtenue en 28x28
        image = cv2.resize(image,(28,28))
        
        IMGtrain.append(image)
        DIGITS.append(image.reshape(1, -1))
    
    #liste contenant toutes les images d'entraînement en ligne
    traindata = np.array(DIGITS)
    trainData = traindata.reshape(len(traindata),784)
    
    
    
    #Création du modèle KNN et entrainement avec un k prédéfini
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(trainData, trainLabels1)
    
    
    
    #Prédiction du label des images tests
    prediction = model.predict(TEST)
    RESULT.append(list(prediction))
    
    #Labels des images à tester
    
    #BON = np.array([1,2,3,4,5,4,1,6,7,1,5,2,8,4,3,9,1])
    #BON = np.array([5,3,7,6,1,9,5,9,8,6,8,6,3,4,8,3,1,7,2,6,6,2,8,4,1,9,5,8,7,9])
    #BON = np.array([1,2,3,4,5,6,7,3,4,5,6,1,8,2,1,5,8,2,6,8,6,2,3,7,8,2,7])
    #BON = np.array([2,5,3,4,1,3,4,1,8,5,3,9,5,3,8,9,7,5,4,2,7,3,9,9,8,4])
    #BON = np.array([1,2,3,4,5,6,7,3,4,5,6,1,8,2,1,5,8,2,6,8,6,1,2,7,5,3,7,5,2,8,8,6,7,2,7,8,3,6,1,5,5,3,7,6,1,9,5,9,8,6,8,6,3,4,8,3,1,7,2,6,6,2,8,4,1,9,5,8,7,9,1,2,3,4,5,4,1,6,7,1,5,2,8,4,3,9,1,2,5,3,4,1,3,4,1,8,5,3,9,5,3,8,9,7,5,4,2,7,3,9,9,8,4])
    BON = [5,3,7,6,1,9,5,9,8,6,8,6,3,4,8,3,1,7,2,6,6,2,8,4,1,9,5,8,7,9,1,2,3,4,5,4,1,6,7,1,5,2,8,4,3,9,1,2,5,3,4,1,3,4,1,8,5,3,9,5,3,8,9,7,5,4,2,7,3,9,9,8,4,1,2,3,4,5,6,7,3,4,5,6,1,8,2,1,5,8,2,6,8,6,1,2,7,5,3,7,5,2,8,8,6,7,2,7,8,3,6,1,5,1,2,4,9,4,5,6,3,9,2,3,6,9,2,1,5,4,6,9,1,5,4,7,8,2,3,6,8,7,4,1,7,4,1,9,5,2,6,2,1,6,5,7,8,3,9,3,8,7,4,1,3,1,9,5,3,2,1,7,6,5,4,6,1,5,2,9,4,7,7,8,3,6,2,9,1,5,7,4,2,8,1,6,1,8,7,6,5,9,2,2,3,6,1,5,4,7,4,2,8,1,3,9,8,3,6,7,1,2,5,5,6,9,2,3,4,8,3,6,1,8,7,8,4,4,8,2,5,6,8,7,5,4,1,6,2,9,9,4,8,3,8,5,6,7,6,4,7,9,2,3,6,4,2,1,9,3,5,1,8,6,3,1,9,4,7,9,4,7,2,8,9,9,5,2,4,1,4,2,1,6,9,1,6,8,7,2,5,5,7,1,2,9,1,7,6,9,7,6,5,3,7,6,5,9,1,5,9,2,4,1,4,6,2,9,1,7,8,6,9,7,9,6,8,9,7,5,5,3,6,1,8,7,1,8,5,6,8,4,7,1,7,5,1,8,9,3,7,2,6,2,1,3,2,5,4,2,9,3,6,5,6,2,9,3,7,6,5,2,5,7,2,4,2,3,1,7,5,8,9,5,2,3,4,1,7,3,6,1,4,2,5,3,5,8,1,4,6,7,1,4,2,7,1,2,9,3,9,6,3,5,8,3,3,6,7,9,6,5,4,9,3,4,7,9,6,8,8,4,6,7,4,1,6,5,5,9,3,7,8,7,4,8,2,1,3,5,2,9,1,3,9,2,5,1,6,6,2,7,7,8,9,4,5,1,3,8,7,4,3,9,4,2,1,3,1,2,9,7,4,4,1,2,7,8,9,8]

    
    #Boucle pour évaluer notre modèle sur les images issues de la grille
    def testimage(dirpath,imax):
        TEST1 = []

        for i in range(1,imax):
            
            filename = str(i)+'.png'
            TEST1.append(test(filename,dirpath,model))
        TEST1 = np.array(TEST1)
        return TEST1
    #ACC.append(accurate(TEST1,BON[0:31])[0])
    #print(accurate(TEST1,BON))