import random as r
def couleur_aleatoire():
    '''Cette fonction ne prend pas de parametre
    et renvoie un triplet de valeur entre
    0 et 255 (code pour les couleurs)'''
    red=r.randint(0,255)
    green=r.randint(0,255)
    blue=r.randint(0,255)
    return (red,green,blue)

##print(couleur_aleatoire())