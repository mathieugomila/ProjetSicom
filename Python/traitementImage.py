# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:40:38 2021

@author: cmbbd
"""
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import Détection_grille_5_0 as D5
import recochiffre4 as r4

def main(filepath):
    casesremplies = (D5.Blanche<D5.seuil)*1
    TEST = []
    TEST= r4.testimage(r"..\Projet Sudoku\TEST\\", np.sum(casesremplies)+1) 
    
    l = 0
    for i in range(len(casesremplies)):
        for j in range(len(casesremplies[0])):
            if (casesremplies[i,j]==1):
                casesremplies[i,j] = TEST[l]
                l+=1
    #print(casesremplies)

    return casesremplies, D5.angle_rot, D5.xsg, D5.xsd, D5.xid, D5.xig, D5.ysg, D5.ysd, D5.yid, D5.yig
    #D5.angle_rot