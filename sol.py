# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:29:00 2022

@author: robin
"""

import turtle as t
def sol(y):
    '''Cette fonction prend un parametre un float representant la hauteur
    du sol
    Elle va dessiner un trait de 710xp commencant en abscisse -400'''

    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"

    t.penup()
    t.setposition(-400,y)
    t.pendown()
    t.fd(710)

##sol(1)
##sol("a")
##t.exitonclick()