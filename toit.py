import toit1 as t1
import toit2 as t2
import trait as t
import random as r
def toit(x,y,niveau):
    '''Cette fonction prend en parametre 3 variable de type integer,
    'x' l'abscisse du milieu de l'immeuble
    'y' l'ordonnee du niveau du sol
    'niveau' le nombre d'etage
    Elle a 40% de chance de dessiner un toit plat et 60% de chance un toit
    triangulaire.'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou integer"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou integer"
    assert type(niveau)==int, "niveau doit etre de type int"

    choix=r.randint(1,10)
    if choix<4:
        #toit plat
        t1.toit1(x,y,niveau)
    else:
        #toit triangulaire
        t2.toit2(x,y,niveau)

##toit(10,10,1)
##toit("a",10,10)
##t.exitonclick()