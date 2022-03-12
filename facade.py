import rectangle as r
import turtle as t
def facade(x,y,couleur,niveau):

    '''Cette fonction prend en parametre 3 float et un triplet d'float
    'x' et 'y' pour les coordonnee du milieu du bas de l'immeuble
    'couleur' represente le code pour la couleur de la porte
    'niveau' le nombre d'etage de l'immeuble
    Elle trace un rectangle de 140xp de large et 60xp de haut pour
    chaques etages, le rectangle sera colore de la couleur donnee'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(couleur)==tuple, "couleur doit etre de type tuple"
    assert type(niveau)==int, "niveau doit etre de type int"

    t.colormode(255)
    t.begin_fill()
    t.fillcolor(couleur)
    r.rectangle(x,y,140,niveau*60)
    t.end_fill()

facade(10,10,(100,100,100),5)
##facade("a",10,10,10)
t.exitonclick()