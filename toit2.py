import turtle as t
import trait as tr
def toit2(x,y,niveau):
    '''Cette fonction prend en parametre 2 variables de type float et un int,
    'x' l'abscisse du milieu de l'immeuble
    'y' l'ordonnee du niveau du sol
    'niveau' le nombre d'etage
    Elle va dessiner un toit triangulaire de hauteur 40px et de base 140px'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(niveau)==int, "niveau doit etre de type int"

    t.pensize(10)
    t.begin_fill()
    t.fillcolor('black')
    tr.trait(x-70, y+niveau*60, x, y+niveau*60+40)
    tr.trait(x, y+niveau*60+40, x+70, y+niveau*60)
    tr.trait(x+70, y+niveau*60, x-70, y+niveau*60)
    t.end_fill()
    t.pensize(1)

##toit2(10,10,2)
##toit2("a",10,2)
##t.exitonclick()