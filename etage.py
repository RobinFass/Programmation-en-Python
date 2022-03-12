import turtle as t
import facade as fa
import rectangle as re
import random as ra
import fenetre as fe
import fenetre_balcon as feb
import porte as p
import couleur_aleatoire as ca
def etage(x,y,couleur,niveau):
    '''Cette fonction prend en parametre 2 float, un int et un triplet d'integer
    'x' et 'y' pour les coordonnee du milieu du bas de l'immeuble
    'couleur' represente le code pour la couleur de la porte
    'niveau' le nombre d'etage de l'immeuble
    Elle delimite chaque etage et attribut aleatoirement les fenetre et
    porte fenetre
    Pour le rez de chausse un porte est mis aleatoirement et les autres
    emplacement sont combles par des fenetre'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(couleur)==tuple, "couleur doit etre de type tuple"
    assert type(niveau)==int, "niveau doit etre de type int"

    re.rectangle(x,y,140,60)
    if niveau==0:
        #rdc
        rand1=ra.randint(-1,1)
        p.porte(x+140/3*rand1,y,couleur)

        if rand1==0:
            #porte au mileu
            fe.fenetre(x-140/3,y+17)
            fe.fenetre(x+140/3,y+17)
        elif rand1==1:
            #porte a droite
            fe.fenetre(x,y+17)
            fe.fenetre(x-140/3,y+17)
        else:
            #porte a gauche
            fe.fenetre(x,y+17)
            fe.fenetre(x+140/3,y+17)
    else:
        #etage
        for i in range (-1,2):
            rand2=ra.randint(1,10)
            if rand2<4:
                feb.fenetre_balcon(x+i*140/3,y)
            else:
                fe.fenetre(x+i*140/3,y+17)

##etage(10,10,(100,100,100),3)
##etage("a",10,10,10)
##t.exitonclick()
