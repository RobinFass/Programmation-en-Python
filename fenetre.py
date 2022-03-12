import rectangle as re
import turtle as t
import trait as tr
import random as ra
def fenetre(x,y):
    '''Cette fonction prend en parametre 2 integer representant les coordonnees
    du milieu de la largueur du bas de la fenetre
    Il y a 40% de chance que la fenetre soit "decoree" et 60% de chance qu'elle
    ne le soit pas.
    La fenetre et un carre de 30px de cote'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou integer"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou integer"

    t.begin_fill()
    t.fillcolor('white')
    re.rectangle(x,y,30,30)
    t.end_fill()

    j=ra.randint(0,10)
    if j>6:
        t.begin_fill()
        t.fillcolor((240,87,33))
        re.rectangle(x-15/2,y,14,30)
        re.rectangle(x+15/2,y,14,30)
        t.end_fill()

        t.pencolor('brown')
        t.pensize(2)
        tr.trait(x-15/3*2,y+2,x-15/3*2,y+28)
        tr.trait(x-15/3,y+2,x-15/3,y+28)

        tr.trait(x+15/3*2,y+2,x+15/3*2,y+28)
        tr.trait(x+15/3,y+2,x+15/3,y+28)

        t.pencolor((60,12,1))
        t.pensize(1)
        tr.trait(x-15/3*2+1,y+4,x-15/3*2+1,y+26)
        tr.trait(x-15/3+1,y+4,x-15/3+1,y+26)

        tr.trait(x+15/3*2+1,y+4,x+15/3*2+1,y+26)
        tr.trait(x+15/3+1,y+4,x+15/3+1,y+26)

        t.pencolor("black")
        t.pensize(1)

##fenetre(10,10)
##fenetre("a",10)
##t.exitonclick()


