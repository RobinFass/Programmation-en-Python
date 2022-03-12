def liste(a,b):
    #La fonction prend en parametre deux nombre (type int) qui representent les
    #les borne de la liste et renvoie une liste de tout les nombre
    #entier de 'a' jusqu'a 'b'.
    liste=[x for x in range(a,b+1)]
    return liste

def divise(nbr,liste):
    #La fonction prend en parametre le nombre du joueur (type int) et la liste
    #des nombres entier borne par les valeur donnees en amont (type int)
    #Appel recurcif et renvoie le nombre en cas de base
    ##Cette fonction s'occuper de la partie diviser et regrouper de principe
    ##diviser pour regner
    global COMPTE
    COMPTE+=1
    l1=[]

    if nbr==liste[0]:
        return "ton nombre est %s" %liste[0]

    for loop in liste[len(liste)//2:]:
        if nbr==loop:
            l1=liste[len(liste)//2:]

    if not l1:
        return divise(nbr,liste[:len(liste)//2])

    return divise(nbr,l1)

def jeu():
    #La fonction ne prend pas de parametre
    #Demande le nombre au joueur et appel les autres fonctions
    #Renvoie le nombre du joueur avec le nombre de coups pour y arriver

    global COMPTE
    petit=int(input("Valeur minimum"))
    grand=int(input("Valeur maximum"))
    nbr=int(input("Choisi un nombre en %s et %s"%(petit,grand)))

    if not petit<nbr<grand:
        return "Le nombre choisi n'est pas dans l'interval donne"

    ##La ligne suivante est la partie regner du principe diviser pour regner
    fin=divise(nbr,liste(petit,grand))+", je l'ai touvé en %s coups" %COMPTE
    COMPTE=0
    return fin

print("ceci %s le %s de %s-%s" %("est","projet","fasseler","robin"))
COMPTE=0