# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:29:00 2022

@author: robin
"""

import immeuble as imm
import sol as s
import turtle as t
#setup vitesse, visibilite du curseur et taille de la fenetre d'affichage
t.speed(0)
t.hideturtle()
t.setup(1500,1000)

def main(x=-400,y=-200):
    '''Cette fonction peux prendre 2 parametres
    'x' et 'y' coordonnees du point ou commence le sol, si aucune valeur n'est
    entree le sol commencera en -400,-200
    Elle dessin une ville de 4 immeubles'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"

    s.sol(y)
    for z in range (0,4):
        imm.immeuble(x+z*710/4+710/8, y)

#execution du programme
main()
print("Ceci est le programme de Steeve, Robin et Max")
t.exitonclick()