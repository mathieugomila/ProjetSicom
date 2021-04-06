# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 18:39:44 2021

@author: Benjamin
"""

import numpy as np
import skimage.transform as skt
import skimage.io as skio
import skimage.color as skc
import matplotlib.pyplot as plt
from scipy import signal
import skimage.util as sku
import cv2
import skimage as sk

plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['figure.max_open_warning'] = 1000
plt.close('all')   

#Renvoie l'indice du min d'une liste compris entre i et j
def index_min_sous_conditions(L,i,j):
    pivot=np.max(L)
    for k in range(len(L)):
        if L[k]<i or L[k]>j:
            L[k]=pivot+1
    return L.index(np.min(L))

#Renvoie l'indice du max d'une liste compris entre i et j
def index_max_sous_conditions(L,i,j):
    pivot=np.min(L)
    for k in range (len(L)):
        if L[k]<i or L[k]>j:
            L[k]=pivot-1
    return L.index(np.max(L))

#Renvoie a,b pour y=ax+b d'une droite défini par 2 points (utilisé avec ligne hough, impossible d'avoir ligne verticale)
def eq_droite(x0,y0,x1,y1):
    if x1==x0 : return x0,np.inf
    a=(y1-y0)/(x1-x0)
    b=y0-a*x0
    return a,b


#Renvoie l'abscisse d'une droite pour une ordonnée
def x_sachant_y(a,b,y):
    if a==0 : x=9999999999999999999
    else : x=(y-b)/a
    return x

#Renvoie l'ordonnée d'une droite pour une abscisse
def y_sachant_x(a,b,x):
    y=a*x+b
    return y

#Renvoie parmi plusieurs droites, les 2 qui sont dans un coin données
#Fraction sert à éliminer les possibles lignes en haut provoqué par une rotation
#coin=0->sup.gauche//coin=1->sup.droit//coin=2->inf.gauche//coin=3->inf.droit
def droites_coin(DROITE,L,C,coin,fraction):
    x=0
    y=0
    les_y=[0]*len(DROITE)
    les_x=[0]*len(DROITE)
    for i in range(len(DROITE)):
        les_y[i]=y_sachant_x(DROITE[i,0],DROITE[i,1],x)
        les_x[i]=x_sachant_y(DROITE[i,0],DROITE[i,1],y)
    if coin==0:
        d1=index_min_sous_conditions(les_y,fraction*L,L)
        d2=index_min_sous_conditions(les_x,0,C)
    elif coin==1:
        d1=index_min_sous_conditions(les_y,fraction*L,L)
        d2=index_max_sous_conditions(les_x,0,C)
    elif coin==2:
        d1=index_max_sous_conditions(les_y,0,L)
        d2=index_min_sous_conditions(les_x,0,C)
    else :
        d1=index_max_sous_conditions(les_y,0,L)
        d2=index_max_sous_conditions(les_x,0,C)
    return d1,d2

#Renvoie l'intersection entre 2 droites
def coordonnees_coin(a1,b1,a2,b2):
    x=round((b2-b1)/(a1-a2))
    y=round(a1*x+b1)
    return x,y
        
#Sur une grille penché, trouve une droite qui sera horizontal après rotation
def trouve_angle_droite_horiz(L,V):
    accum=0
    compteur=0
    for i in range (len(L)):
        if L[i]>np.pi/4 and V[0,i]==1:
            accum+=L[i]
            compteur+=1
        elif L[i]<(-np.pi/4) and V[0,i]==1:
            accum+=(L[i]+np.pi)
            compteur+=1
    if compteur!=0:
        return accum/compteur
    else :
        return "Erreur d'angle \n"

#Renvoie la liste des angles de droite sans celles où l'angle n'est pas 0 ou pi/2 à une tolérance près
def tri_angle(liste):
    n=len(liste)
    liste_angles_corrects=np.ones((1,n))
    compteur_faux=0
    for i in range(n):
        if liste[i]>0.26 and liste[i]<1.31:
            liste_angles_corrects[0,i]=0
            compteur_faux+=1
    return liste_angles_corrects,(n-compteur_faux)

#Recadre une image en ne conservant qu'une fraction des lignes et colonnes
def recadrage_chiffre(chiffre,fraction):
    L,C=np.shape(chiffre)
    x_inf=round(C*(1-fraction))
    x_sup=round(C*fraction)
    y_inf=round(L*(1-fraction))
    y_sup=round(L*fraction)
    return chiffre[y_inf:y_sup,x_inf:x_sup]
    
#Recherche si une image donnée est blanche ou contient un chiffre
def image_blanche(image):
    compteur=0
    nb_pixel=0
    for i in range(len(image)):
        for j in range(len(image[0])):
            nb_pixel+=1
            if image[i,j]>128:
                compteur+=1
    compteur=compteur/nb_pixel
    return compteur

def noir_sur_contour(image):
    L,C=np.shape(image)
    for i in range(L):
        if image[i,0]==0:
            image[i,0]=255
            return image,i,0
        if image[i,C-1]==0:
            image[i,C-1]=255
            return image,i,C-1
    for j in range(C):
        if image[0,j]==0:
            image[0,j]=255
            return image,0,j
        if image[L-1,j]==0:
            image[L-1,j]=255
            return image,L-1,j
    return image,L+1,C+1

def efface_voisinage(truc_a_manger,image,i,j):
    L,C=np.shape(image)
    truc_a_manger[i,j]=1
    if (i-1)>0 and (image[i-1,j]==0 and truc_a_manger[i-1,j]!=1):
        truc_a_manger[i-1,j]=1
        truc_a_manger=efface_voisinage(truc_a_manger,image,i-1,j)
        
    if (i+1)<L and (image[i+1,j]==0 and truc_a_manger[i+1,j]!=1):
        truc_a_manger[i+1,j]=1
        truc_a_manger=efface_voisinage(truc_a_manger,image,i+1,j)
        
    if (j-1)>0 and (image[i,j-1]==0 and truc_a_manger[i,j-1]!=1):
        truc_a_manger[i,j-1]=1
        truc_a_manger=efface_voisinage(truc_a_manger,image,i,j-1)
        
    if (j+1)<C and (image[i,j+1]==0 and truc_a_manger[i,j+1]!=1):
        truc_a_manger[i,j+1]=1
        truc_a_manger=efface_voisinage(truc_a_manger,image,i,j+1)
    return truc_a_manger
        
#A partir d'une image où des lignes touchent les bords, efface ces lignes
def mange_ligne(image,L,C):
    fraction=100/L #A REGLER : % pour le resize
    image=cv2.resize(image,(int(fraction*L),int(fraction*C)))
    image=sk.img_as_ubyte(image)
    ret,image=cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    L,C=np.shape(image)
    truc_a_manger=np.zeros((L,C))
    image,a,b=noir_sur_contour(image)
    while(a!=L+1 and b!=C+1):
        truc_a_manger=efface_voisinage(truc_a_manger,image,a,b)
        image,a,b=noir_sur_contour(image)
    for i in range(L):
        for j in range(C):
            if truc_a_manger[i,j]==1:
                image[i,j]=255
    return image
    
def extrait_chiffre(image,seuil_aire):
    L,C=np.shape(image)
    thresh=mange_ligne(image,L,C)
    thresh[0,0]=0 #Sinon, si il y a que des 255, affiche en écran noir alors que c'est tout blanc
    thresh=sku.invert(thresh)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_cnt=0
    for cnt in contours :
        if cv2.contourArea(cnt)>max_cnt :
            max_cnt=cv2.contourArea(cnt)
            cnt_chiffre=cnt
    if max_cnt>seuil_aire:
        # on récupère le rectangle encadrant le chiffre
        brect = cv2.boundingRect(cnt_chiffre)
        x,y,w,h = brect
        # extraction de notre "region of interest"
        # notre roi correspond à un chiffre sur notre feuille
        roi = thresh[y:y+h, x:x+w]
        return sku.invert(roi)
    else :
        return sku.invert(thresh)

            
#Retourne une grille 9*9 avec la présence de chiffre ou non de chaque case de image ; case_grille contient les 4 coordonnées des coins de chaque case
def case_blanche(image,case_grille,ind_recadrage):
    PRESENT=np.zeros((9,9))
    for i in range(len(case_grille)):
        for j in range (len(case_grille[0])):
            case=image[case_grille[i,j,2]:case_grille[i,j,3],case_grille[i,j,0]:case_grille[i,j,1]]
            case=sk.img_as_ubyte(case)
            case=extrait_chiffre(case,40) #Seuil_aire à 40 vu qu'on resize la case à 100 environ en début de mange_ligne
            affiche_image(case,"chiffre")
            PRESENT[i,j]=image_blanche(case)
    return PRESENT

#Retourne les positions des angles perpendiculaires de L à une tolérance tol près
def angles_perpendic(L,tol):
    V=np.zeros((1,len(L)))
    for i in range (len(L)):
        obs=L[i]
        for j in range(len(L)):
            if obs>0:
                if L[j]>obs-(np.pi/2)-tol and L[j]<obs-(np.pi/2)+tol:
                    V[0,i]=1
            else : #obs<0
                if L[j]>obs-(np.pi/2)-tol and L[j]<obs-(np.pi/2)+tol:
                    V[0,i]=1
    return V

#Ouvre une image en niveau de gris
def ouvre_image_gris(chemin):
    image=skio.imread(chemin)
    image=skc.rgb2gray(image)
    return image

#Affiche une image dans une nouvelle fenêtre
def affiche_image(image,titre):
    plt.figure()
    plt.imshow(image), plt.title(titre)

#Calcule la magnitude du gradient d'une image
def gradient_image(image):
    scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],
                   [-10+0j, 0+ 0j, +10 +0j],
                   [ -3+3j, 0+10j,  +3 +3j]]) # Gx + j*Gy
    grad = signal.convolve2d(image, scharr, boundary='symm', mode='same')
    Mag=np.absolute(grad)
    return Mag

#Affiche les lignes de la tranformée de Hough d'image_ligne sur image_fond
def affiche_ligne_hough(image_fond,image_ligne,titre):
    hspace,theta,d=skt.hough_line(image_ligne)
    origin = np.array((0, image_ligne.shape[1]))
    affiche_image(image_fond,titre)
    for _, angle, dist in zip(*skt.hough_line_peaks(hspace, theta, d)):
        if angle==0 : angle+=10**(-7)
        y0, y1 = (dist - origin * np.cos(angle)) / np.sin(angle)
        plt.plot(origin,(y0,y1),color='black')
    plt.xlim(origin)
    plt.ylim((image_ligne.shape[0], 0))
    

#Récupération de la grille
grille=ouvre_image_gris('test.jpg')
L,C=np.shape(grille)
affiche_image(grille,'Image original')

#Gradient
Mag=gradient_image(grille)

grille_degrade=np.copy(grille)
#Elimintation des dégradés de luminosité
for i in range(L):
    for j in range(C):
        if Mag[i,j]<1:
            grille_degrade[i,j]=1

affiche_image(grille_degrade,'Image dégradé')
           

#Seuillage des points de contour
Mag=gradient_image(grille_degrade)
M=np.max(Mag)
seuil=M*0.2    #coef_seuil 
grille_bin=(Mag>seuil)*1
affiche_image(grille_bin,'Grille_binaire')
affiche_ligne_hough(grille_degrade,grille_bin,"Lignes sur l'image à traiter") 

#Repositionne la grille droite
hspace,theta,d=skt.hough_line(grille_bin)
_,L_angle,_=skt.hough_line_peaks(hspace,theta,d)
Angles_valides=angles_perpendic(L_angle,0.07) #tolerance=0.07
angle_rot=trouve_angle_droite_horiz(L_angle,Angles_valides)-(np.pi/2)
print('angle_rot=',angle_rot*180/np.pi,'degré')
grille_rep=skt.rotate(grille_bin,angle_rot*180/np.pi,preserve_range=True)
grille_or_rep=skt.rotate(grille,angle_rot*180/np.pi,preserve_range=True)
affiche_image(grille_rep,'grille_rep')

#La rotation a abîmé la finesse du gradient
M=np.max(grille_rep)
seuil=M*0.40
grille_rep_bin=(grille_rep>seuil)*1
affiche_image(grille_rep_bin,'Grille repositionnée binaire')

#Désormais, la grille est droite, nous sommes sûr que les angles des droites sont 0 ou pi/2 (ou presque)
#Transformée de Hough
hspace,theta,d=skt.hough_line(grille_rep_bin)
_,angles,_=skt.hough_line_peaks(hspace,theta,d)
angles_corrects,nb_lignes=tri_angle(np.abs(angles)) #Donne les indices où les droites ne sont pas des diagonales
DROITE=np.zeros((nb_lignes,2)) #Tableau avec a et b de chaque droite
origin = np.array((0, grille_rep_bin.shape[1]))
i=0
affiche_image(grille_or_rep,'Détection coins')
    #Calcul d'équation des lignes détectés
for _, angle, dist in zip(*skt.hough_line_peaks(hspace, theta, d)): #ICI, condition pour ignorer angle incorrect
    if angles_corrects[0,i]==1: #Si on ne traite pas une diagonale
        if angle==0 : angle+=10**(-7)
        y0, y1 = (dist - origin * np.cos(angle)) / np.sin(angle)
        DROITE[i,0],DROITE[i,1]=eq_droite(origin[0],y0,origin[1],y1)
        plt.plot(origin,(y0,y1),color='black')
        i+=1
plt.xlim(origin)
plt.ylim((grille_rep_bin.shape[0], 0))


#Recherche coin supérieur gauche
ind_d1,ind_d2=droites_coin(DROITE,L,C,0,0.05)
xsg,ysg=coordonnees_coin(DROITE[ind_d1,0],DROITE[ind_d1,1],DROITE[ind_d2,0],DROITE[ind_d2,1])

#Recherche coin supérieur droit
ind_d1,ind_d2=droites_coin(DROITE,L,C,1,0.05)
xsd,ysd=coordonnees_coin(DROITE[ind_d1,0],DROITE[ind_d1,1],DROITE[ind_d2,0],DROITE[ind_d2,1])

#Recherche coin inférieur gauche
ind_d1,ind_d2=droites_coin(DROITE,L,C,2,0.1)
xig,yig=coordonnees_coin(DROITE[ind_d1,0],DROITE[ind_d1,1],DROITE[ind_d2,0],DROITE[ind_d2,1])

#Recherche coin inférieur droit
ind_d1,ind_d2=droites_coin(DROITE,L,C,3,0.1)
xid,yid=coordonnees_coin(DROITE[ind_d1,0],DROITE[ind_d1,1],DROITE[ind_d2,0],DROITE[ind_d2,1])

plt.scatter([xsg,xsd,xig,xid],[ysg,ysd,yig,yid],s=100,c='red',marker='x')

pas_vert_inf=yig-ysg;pas_vert_inf=(pas_vert_inf/9)
pas_horiz_inf=xsd-xsg;pas_horiz_inf=(pas_horiz_inf/9)
pas_vert_sup=yid-ysd;pas_vert_sup=(pas_vert_sup/9)
pas_horiz_sup=xid-xig;pas_horiz_sup=(pas_horiz_sup/9)

#On cherche les angles des pas pour contrer la perspective
dec_x_inf=xsg-xig
dec_x_sup=xsd-xid
dec_y_inf=ysd-ysg
dec_y_sup=yid-yig

#Grille des coordonnées des coins des cases
#0:x inf,1:x sup,2:y inf,3:y haut

new_grille=np.zeros((9,9,4),dtype=np.uint32)
dezoom=0.02*L
#les y donnent les gammes de lignes et les x les gammes de colonnes
for k in range(0,9):
    if k<4:
        pas_horiz=pas_horiz_inf
    else:
        pas_horiz=pas_horiz_sup
    for l in range(0,4):
        if k<4:
            new_grille[k,l,0]=xsg+(l*pas_horiz)-dezoom
            new_grille[k,l,2]=ysg+(k*pas_vert_inf)-dezoom
        else :
            new_grille[k,l,0]=xig+(l*pas_horiz)-dezoom
            new_grille[k,l,2]=yig-((9-k)*pas_vert_inf)-dezoom
        new_grille[k,l,1]=new_grille[k,l,0]+pas_horiz+2*dezoom
        new_grille[k,l,3]=new_grille[k,l,2]+pas_vert_inf+2*dezoom
    for l in range(4,9):
        if k<4:
            new_grille[k,l,0]=xsd-((9-l)*pas_horiz)-dezoom
            new_grille[k,l,2]=ysd+(k*pas_vert_sup)-dezoom
        else : 
            new_grille[k,l,0]=xid-((9-l)*pas_horiz)-dezoom
            new_grille[k,l,2]=yid-((9-k)*pas_vert_sup)-dezoom
        new_grille[k,l,1]=new_grille[k,l,0]+pas_horiz+2*dezoom
        new_grille[k,l,3]=new_grille[k,l,2]+pas_vert_sup+2*dezoom
        
image_bis=grille_or_rep[new_grille[8,7,2]:new_grille[8,7,3],new_grille[8,7,0]:new_grille[8,7,1]]
affiche_image(image_bis,'Case à regarder')

Blanche=case_blanche(grille_or_rep,new_grille,0.75)
L_B,C_B=np.shape(Blanche)
compteur=1
seuil=0.90 #Seuil pour determiner case vide ou non
sauv=1 #Sauvegarde-t-on les cases ?
for i in range(L_B):
    for j in range(C_B):
        if Blanche[i,j]<seuil:
            image=grille_or_rep[new_grille[i,j,2]:new_grille[i,j,3],new_grille[i,j,0]:new_grille[i,j,1]]
            image=extrait_chiffre(image, 40) #Seuil_aire à 40 vu qu'on resize la case à 100 environ en début de mange_ligne
            if (sauv==0) : affiche_image(image,'Chiffre de la case')
            image=sk.img_as_ubyte(image)
            titre='TEST/'+str(compteur)+'.png'
            if (sauv):
                skio.imsave(titre,image)
            compteur+=1

print(compteur-1)

#On peut directement renvoyer le chiffre extrait



