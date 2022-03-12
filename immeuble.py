import turtle as t
import facade as fa
import random as ra
import etage as e
import couleur_aleatoire as ca
import toit as toi #hehe
def immeuble(x,y):
    '''Cette fonction prend en parametre 2 float
    'x' et 'y' pour les coordonnee du milieu du cote situe en bas de l'immeuble
    Elle prend un nombre aleatoire entre 1 et 5 pour les etages et selectionne
    une couleur
    Elle dessin tout un immeuble '''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"

    nbr_etages=ra.randint(1,5)
    fa.facade(x,y,ca.couleur_aleatoire(),nbr_etages)
    for i in range(nbr_etages):
        c=ca.couleur_aleatoire()
        e.etage(x,y+i*60,c,i)
    toi.toit(x,y,nbr_etages)

##immeuble(10,10)
##immeuble("a",10)
##t.exitonclick()