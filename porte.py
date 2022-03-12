import rectangle as re
import turtle as t
import random as ra
def porte(x,y,couleur):
    '''Cette fonction prend en parametre 2 integer et un triplet de integer
    'x' et 'y' represente les coordonnees du milieu du bas de la porte
    'couleur' represente le code pour la couleur de la porte
    La porte fait 30px de large et 50px de haut et a 40% d'etre arrondi en haut
    et 60% de chance d'etre rectangulaire'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(couleur)==tuple, "couleur doit etre de type int tuple"

    r=couleur[0]
    g=couleur[1]
    b=couleur[2]
    if r>30 and g>30 and b>30:
        couleur=(r-30,g-30,b-30)

    choix=ra.randint(1,10)
    if choix<4:
         #porte rectangle
        porte_rectangle(x,y,couleur)
    else:
        #porte arrondi
        porte_ronde(x,y,couleur)

def porte_rectangle(x,y,couleur):
    '''Cette fonction prend en parametre 2 integer et un triplet de integer
    'x' et 'y' represente les coordonnees du milieu du bas de la porte
    'couleur' represente le code pour la couleur de la porte
    Elle dessin un rectangle de 30xp de large et 50px de haut'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(couleur)==tuple, "couleur doit etre de type int tuple"

    t.colormode(255)
    t.begin_fill()
    t.fillcolor(couleur)
    re.rectangle(x,y,30,50)
    t.end_fill()

def porte_ronde(x,y,couleur):
    '''Cette fonction prend en parametre 2 integer et un triplet de integer
    'x' et 'y' represente les coordonnees du milieu du bas de la porte
    'couleur' represente le code pour la couleur de la porte
    Elle dessin une porte de 30xp de large et 50xp de haut arrondi en haut'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(couleur)==tuple, "couleur doit etre de type int tuple"

    t.colormode(255)
    t.begin_fill()
    t.fillcolor(couleur)
    re.rectangle(x,y,30,40)
    t.penup()
    t.setposition(x+15,y+40)
    t.pendown()

    #trait pour cacher le trait noir fait par le demi cercle
    t.pensize(2)
    t.pencolor(couleur)
    t.setposition(x-15,y+40)

    #set position et couleur
    t.penup()
    t.pencolor('black')
    t.pensize(1)
    t.setposition(x+15,y+38)
    t.pendown()

    #demi cercle
    t.lt(90)
    t.circle(15,180)
    t.penup()
    t.lt(90)

    #set position
    t.setposition(x-15,y)
    t.pendown()
    t.end_fill()

##porte(10,10,(10,10,10))
##porte("a",10,(10,10,10))

##porte_rectangle(10,10,(10,10,10))
##porte_rectangle("a",10,(10,10,10))

##porte_ronde(10,10,(10,10,10))
##porte_ronde("a",10,(10,10,10))
##t.exitonclick()