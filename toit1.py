import turtle as t
import trait as tr
def toit1(x,y,niveau):
    '''Cette fonction prend en parametre 2 variables de type float et un int,
    'x' l'abscisse du milieu de l'immeuble
    'y' l'ordonnee du niveau du sol
    'niveau' le nombre d'etage
    Elle va dessiner un toit plat de 140px'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(niveau)==int, "niveau doit etre de type int"

    t.pensize(10)
    tr.trait(x-70,y+niveau*60,x+70,y+niveau*60)
    t.pensize(1)

##toit1(10,10,2)
##toit1("a",10,2)
##t.exitonclick()