# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:34:52 2021

@author: fasseler_r
"""
import tkinter as tk
import random as r
f=tk.Tk()

def damier(dim=200,carre=10,full=False):
    '''
    Cree un damier carre de carre noir et blanche.
    
    Parameters
    ----------
    dim : INT, optional
        La taille en pixel d'un cote.
        The default is 200.
        
    carre : INT, optional
        Le nombre de carre sur une ligne/colonne. The default is 10.
        
    full : BOOLEEN, optional
        Si True, le damier s'affiche comme un jeu de dame.
        Si False, les carre blanc ont une chance sur deux d'etre noir.
        The default is False.

    Returns
    -------
    Effet de bord.
    None.

    '''
  
    z2d=tk.Canvas(f,width=dim-2,height=dim-2)
    z2d.pack()
    
    z2d.create_rectangle(0,0,dim,dim,fill="black")
    decalage=0
    saute=0
    if full:
        couleur=['white']
    else:
        couleur=['black','white']
    
    for ligne in range(carre):
        for _ in range(carre//2+1):
            z2d.create_rectangle(dim/carre+decalage,0+saute,(dim/carre)*2+decalage,dim/carre+saute,fill=r.choice(couleur))
            decalage+=(dim/carre)*2
        if ligne%2!=0:    
            decalage=0
        else:
            decalage=-(dim/carre)
        saute+=dim/carre
   
dim=int(input("Dimention du damier (en pixels): "))
carre=int(input("Nombre de carres par ligne: "))
try:
    test=int(input("Est ce que le damier doit etre emplie ? (True,1/False,0): "))
except:
    test=False
    
damier(dim,carre,full=test)

f.mainloop()