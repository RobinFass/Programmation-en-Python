import turtle as t
import trait as tr
import rectangle as r
import random as ra
def fenetre_balcon(x,y):
    '''Cette fonction prend en parametre 2 integer representant les coordonnees
    du milieu de la largueur du bas de la porte fenetre
    Il y a 40% de chance que la porte fenetre soit "decoree" et 60% de chance
    qu'elle ne le soit pas.
    La porte fenetre fait 30xp de large et 50px de haut
    Puis elle dessin les barreaux du balcon'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"

    random=ra.randint(0,10)
    t.colormode(255)
    if random>6:
        #porte fenetre "decoree"
        t.begin_fill()
        t.fillcolor((224,206,124))
        r.rectangle(x,y,30,50)
        t.end_fill()
        t.begin_fill()
        t.fillcolor((224,198,68))
        r.rectangle(x+4,y+35,6,15)
        t.end_fill()
    else:
        #porte fenetre normal
        t.begin_fill()
        t.fillcolor('white')
        r.rectangle(x,y,30,50)
        t.end_fill()

    #balcon
    t.pensize(3)
    tr.trait(x-20,y,x+20,y)
    tr.trait(x-20,y+25,x+20,y+25)
    t.pensize(2)
    for n in range (9):
        tr.trait(x-20+n*5,y,x-20+n*5,y+25)
    t.pensize(1)

##fenetre_balcon(10,10)
##fenetre_balcon("a",10)
##t.exitonclick()