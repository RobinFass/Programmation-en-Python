import trait as tr
def rectangle(x,y,w,h):
    '''Cette fonction prend en parametre 4 float
    'x' et 'y' pour les coordonnee du milieu du cote situe en bas du rectangle
    'w' la largueur du rectancle (ici le cote situes en haut et en bas)
    'h' la hauteur du rectangle (ici situes a gauche et a droit de la figure)
    Elle trace un rectangle'''

    assert type(x)==int or type(x)==float, "x doit etre de type int ou float"
    assert type(y)==int or type(y)==float, "y doit etre de type int ou float"
    assert type(w)==int or type(w)==float, "w doit etre de type int ou float"
    assert type(h)==int or type(h)==float, "h doit etre de type int ou float"

    tr.trait(x-w/2,y,x+w/2,y)
    tr.trait(x+w/2,y,x+w/2,y+h)
    tr.trait(x+w/2,y+h,x-w/2,y+h)
    tr.trait(x-w/2,y+h,x-w/2,y)

##import turtle as t
##rectangle("h",10,10,10)
##rectangle(10,10,10,10)
##rectangle(-10,20,-60,34)
##t.exitonclick()