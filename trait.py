import turtle as t
def trait(x1,y1,x2,y2):
    '''Cette fonction prend en parametre 4 integer representant les coordonnées
    de 2 points.
    Elle trace grace a turtle un trait du premier point au deuxieme.'''

    assert type(x1)==int or type(x1)==float, "x1 doit etre de type int ou float"
    assert type(y1)==int or type(y1)==float, "y1 doit etre de type int ou float"
    assert type(x2)==int or type(x2)==float, "x2 doit etre de type int ou float"
    assert type(y2)==int or type(y2)==float, "y2 doit etre de type int ou float"
    t.penup()
    t.setposition(x1,y1)
    t.pendown()
    t.setposition(x2,y2)

##trait(10,10,100,100)
##trait("a",10,10,10)
##t.exitonclick()