# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:54:22 2021

@author: fasseler_r
"""
#importation des bibliotheques utilisees
from tkinter import*
from random import*
fen=Tk()

#recuperation de la taille de l'ecran (variables globales)
LARGEUR=fen.winfo_screenwidth()
HAUTEUR=fen.winfo_screenheight()

#creation du canevas
can=Canvas(fen,width=LARGEUR,height=HAUTEUR-200,bg="#ADD8E6")
can.grid(row=0,column=0,columnspan=3)


def sommet(x,y,nom,color="black"):
    '''
    Cette fonction affiche un sommet et son nom

    Parameters
    ----------
    x : int
        Coordonnee x du sommet
    y : int
        Coordonnee y du sommet
    color : str, optional
        couleur du sommet
        La valeur par default est "black".

    Effet de bord
    ------
    Les methodes "create_oval" et "create_text" sont appliquees au canevas ("can")
    
    Returns
    -------
    None.

    '''
    can.create_oval(x-15,y-15,x+15,y+15,width=2,fill="#ADD8E6",outline=color)
    can.create_text(x,y,text=nom)



def arete(s1,s2,color="black"):
    '''
    Cette fonction affiche 2 sommets et leur arete commune

    Parameters
    ----------
    s1 : tuple
        Tuple des coordonnees du sommet ainsi que sont nom
    s2 : tuple
        Tuple des coordonnees du sommet ainsi que sont nom
    color : str, optional
        couleur de l'arete et du deuxieme sommet
        La valeur par default est "black".

    Effet de bord
    ------
    La fonction "sommet" est applique au 2 sommets, et la methode "create_line"
    est appliquee au canevas ("can")
    
    Returns
    -------
    None.

    '''
    can.create_line(s1[0],s1[1],s2[0],s2[1],width=2,fill=color)
    sommet(s1[0],s1[1],s1[2],color)
    sommet(s2[0],s2[1],s2[2],color)



def dico():
    '''
    Cette fonction prendre le dictionnaire ecris entre dans la zone de text
    et le rend comprehensible par un ordinateur.
    
    Effet de bord
    -------
    Met a jour les variables globales "F3","BOUTON" et "LISTE" qui sont
    respectivement le dictionnaire des coordonnees des sommets, un tuple
    contenant le nom du graphe/dictionnaire ("fin") et le dictionnaire ("dic"),
    et la liste des l'odre des sommets a afficher.
    
    Les fonctions "dico_coo" et "MODE1" sont utilise, ici "MODE1" est une
    variable a qui on a donne le nom des fonctions de recherche dans un graphe

    Returns
    -------
    None.

    '''
    global BOUTON
    global LISTE
    global F3
    global NOIR
    NOIR=[]
    can.delete("all")
    graph=ent.get().split("=")
    fin=graph[0]
    wait=[i for i in graph[1] if i not in ['{','}',':',',','"',']']]
    dic={}
    clef=[]
    value=[]
    sommet=[]
    
    fen.title(fin)
    #separation des therme
    for a in wait:
        if a != "[":
            clef.append(a)
        if a == "[":
            value.append(clef)
            clef=[]
    value.append(clef)

    #creation de deux liste, une les sommets et l'autre les la liste des voisins des sommets
    for ind,i in enumerate(value):
        if ind+1!=len(value):
            sommet.append(i[-1])
            i.remove(i[-1])
    value.pop(0)

    #creation dico
    for ind,val in enumerate(value):
        dic[sommet[ind]]=val

    F3=dico_coo(dic)
    BOUTON=(fin,dic)
    LISTE=MODE1()



def dico_coo(dico):
    '''
    Cette fonction cree des coordonees aleatoires pour chaque sommet du graphe

    Parameters
    ----------
    dico : dictionnaire
        Dictionnaire qui a un sommet associe ces voisins

    Returns
    -------
    coo : dictionnaie
        Dictionnaire qui a un sommet associes une coordonnees d'un plan

    '''
    global LARGEUR
    global HAUTEUR
    coo={}
    for i in dico:
        x=randint(15,LARGEUR-15)
        y=randint(15,HAUTEUR-215)
        coo[i]=(x,y)
    for a in coo:
        for b in coo:
            if a!=b:
                if euclidienne(coo[a],coo[b])<40:
                    coo={}
                    dico_coo(dico)
    return coo



def euclidienne(st1,st2):
    '''
    Cette fonction calcule la distance entre 2 points dans un plan
    
    Parameters
    ----------
    st1 : tuple d'int
        Tuple de coodronnees

    st2 : tuple d'int
        Tuple de coordonees
    -------
    int
        Calcul la distance euclidienne, entre les 2 points
    '''
    return round(((st1[0]-st2[0])**2+(st1[1]-st2[1])**2)**0.5)



def trait(dico,sommet):
    '''
    Cette fonction affiche un sommet et ces voisins
    
    Parametres
    -------
    dico : dictionnaire
        Dictionnaire du graphe en cours d'utilisation
    sommet : str
        Un sommet du graphe/ une clef du dictionnaire
        
    Effet de bord
    -------
    La fonction "arete" est appliquer au sommet et a ces voisins
    
    Returns
    -------
    None.

    '''
    global F3
    for i in dico[sommet]:
        arete([F3[sommet][0] , F3[sommet][1] , sommet] , [F3[i][0] , F3[i][1] , i])



def trait_complet():
    '''
    Cette fonction affiche entierement le graphe donne
    
    Effet de bord
    -------
    La fonction "arete" est appliquer a chaque sommet et ces voisins
    
    Returns
    -------
    None.

    '''
    global BOUTON
    global F3
    global LISTE
    P.set(LISTE)
    if ent3.get()=="":
        color2="black"
    else:
        color2=ent3.get()
        
    for i in BOUTON[1]:
        for a in BOUTON[1][i]:
            arete([F3[i][0] , F3[i][1] , i] , [F3[a][0] , F3[a][1] , a],color2)




def DFS():
    '''
    Recherche en profondeur dans un grpahe
    
    Returns
    -------
    fin : liste
        Liste des sommets dans l'ordre de profondeur
    '''
    global BOUTON
    graphe=BOUTON[1]
    depart=list(BOUTON[1].keys())[0]
    can.delete("all")
    a_visiter=[]
    vu=[]
    vu.append(depart)
    a_visiter.append(depart)
    fin=[]
    while a_visiter != []:
        sommet=a_visiter[0]
        a_visiter=a_visiter[1:]
        fin.append(sommet)

        for sommet_actuel in graphe[sommet]:
            if sommet_actuel not in vu:
                vu.append(sommet_actuel)
                a_visiter=[sommet_actuel]+a_visiter
    return fin



def BFS():
    '''
    Recherche en largeur dans un grpahe
    
    Returns
    -------
    fin : liste
        Liste des sommets dans l'ordre de largeur
    '''
    global BOUTON
    graphe=BOUTON[1]
    depart=list(BOUTON[1].keys())[0]
    can.delete("all")
    a_visiter=[]
    vu=[]
    vu.append(depart)
    a_visiter.append(depart)
    fin=[]
    while a_visiter != []:
        sommet=a_visiter[0]
        a_visiter=a_visiter[1:]
        fin.append(sommet)
        for sommet_actuel in graphe[sommet]:
            if sommet_actuel not in vu:
                vu.append(sommet_actuel)
                a_visiter=a_visiter + [sommet_actuel]
    return fin



def suite():
    '''
    Cette fonction a pour but d'ordonné l'odre de passage des sommets afin
    d'avoir un affichage propre et pas étape.
    
    Effet de bord
    -------
    Les fonctions "arete" et "sommet" sont appliqué a chaque sommet de "LISTE"
    et ces voisins
    
    Returns
    -------
    None.
    '''
    global BOUTON
    global LISTE
    global NOIR
    global F3
    global P
    dico=BOUTON[1]
    
    if ent2.get()=="":
        color="green"
    else:
        color=ent2.get()
        
    if ent3.get()=="":
        color2="black"
    else:
        color2=ent3.get()
        
    if LISTE:
        NOIR.append(LISTE[0])
        P.set(NOIR)
        actu=LISTE[0]
        voisin=dico[LISTE[0]]
        
        sommet(F3[actu][0],F3[actu][1],actu,color2)
        for i in voisin:
            arete((F3[actu][0],F3[actu][1],actu),(F3[i][0],F3[i][1],i),color)
        for a in NOIR:
            if a in voisin:
                arete((F3[actu][0],F3[actu][1],actu),(F3[a][0],F3[a][1],a),color2)
        LISTE.pop(0)


def selec1():
    '''
    Cette fonction met la variable globale "MODE1" sur la recherche
    en profondeur

    Returns
    -------
    None.
    '''
    global MODE1
    MODE1=DFS


def selec2():
    '''
    Cette fonction met la variable globale "MODE1" sur la recherche
    en largeur

    Returns
    -------
    None.
    '''
    global MODE1
    MODE1=BFS
    
    
#creation des variables globales
BOUTON=0
LISTE=0
F3=0
NOIR=[]
P=StringVar()
MODE1=DFS

#graphe test
graphe_1={"A":["B","E"],"B":["A","D","C"],"C":["B","F"],"D":["B","E","F"],"E":["A","D"],"F":["D","C"]}

#phrase expliquant l'utilite de la zone de text en dessosu
tpile=Label(fen,text="Pile de l'ordre du graphe :")
tpile.grid(row=1,column=0)

#zone de text mis a jour automatiquement avec la progression dans le parcours
#du graphe
pile=Label(fen,textvariable=P)
pile.grid(row=2,column=0)

#phrase serrant a expliquer l'utilisation de la zone de text en dessous
text=Label(fen,text="Un dictionnaire representant le graphe :")
text.grid(row=1,column=1)

#zone de text pour la saisi du dictionnaire
ent=Entry(fen,width=50)
ent.grid(row=2,column=1)

#selection du mode de recherche/affichage
#fonction "selec1" et "selce2" utilise
radioValue=IntVar()
rad=Radiobutton(fen,text="DFS",variable=radioValue,value=1,command=selec1,indicatoron=0)
rad2=Radiobutton(fen,text="BFS",variable=radioValue,value=2,command=selec2,indicatoron=0)
rad.grid(row=3,column=0)
rad2.grid(row=4,column=0)

#phrase serrant a expliquer l'utilisation de la zone de text en dessous
text2=Label(fen,text="Couleur des nouveaux sommets, en toute lettre/hexadicimal :")
text2.grid(row=1,column=2)

#zone de text pour la saisi du dictionnaire
ent2=Entry(fen,width=50)
ent2.grid(row=2,column=2)

#phrase serrant a expliquer l'utilisation de la zone de text en dessous
text3=Label(fen,text="Couleur du graphe, en toute lettre/hexadicimal :")
text3.grid(row=3,column=2)

#zone de text pour la saisi du dictionnaire
ent3=Entry(fen,width=20)
ent3.grid(row=4,column=2)

#validation du dico entrer et reste du canevas si deja utiliser
#fonction "dico" utilise
b=Button(fen,text="Valide/Reset",command=dico)
b.grid(row=3,column=1)

#affichage du graphe entierement sans etapes/fonction "suite"
#fonction "trait_complet" utilise
b1=Button(fen,text="Affiche le graphe entierement",command=trait_complet)
b1.grid(row=4,column=1)

#affichage par etape du graphe
#fonction "suite" utilise
suivant=Button(fen,text="Suivant",command=suite)
suivant.grid(row=5,column=1)

#destruction de la fenetre
quitte=Button(fen,text="Quitter",command=fen.destroy)
quitte.grid(row=6,column=1)


fen.mainloop()