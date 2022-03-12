# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:30:38 2021

@author: fasseler_r
"""
import random as r
from tkinter import*
import time as t
fen=Tk()

#creation du canevas
can=Canvas(fen,width=502,height=502,bg="#ADD8E6")
can.grid(row=1)

MEMO=[]

class Case:
    def __init__(self,valeur=False,affiche='-'):
        self.val=valeur
        self.aff=affiche

    def est_piegee(self):
        return self.val

    def conversion(self):
        self.val=None

    def getval(self):
        return self.val

    def __str__(self):
        return str(self.val)

def genere_jeu(n,p,k):
    '''
    cree un tableaux consituer d'une liste de liste de True ou False

    Parameters
    ----------
    n : int
        le nombre de lignes.
    p : int
        le nombre de colonnes.
    k : int
        le nombres de bombes.

    Returns
    -------
    jeu : list
        La grille de jeu.

    '''
    assert type(n) and type(p) and type(k) == int, "Type: n, p et k doivent etre des integers"
    assert n*p>k, "La quantite de mines doit etre inferieur au nombres de cases"
    jeu=[]
    for i in range(n):
        ligne=[]
        for y in range(p):
            ligne.append(Case(True))
        jeu.append(ligne)

    memoire=[]
    while k>0:
        nn=r.randint(0, n-1)
        pp=r.randint(0, p-1)
        if not (nn,pp) in memoire:
            jeu[nn][pp]=Case(False)
            k-=1
        memoire.append((nn,pp))
    return jeu

def traitement_case(jeu,n,p):
    '''
    donne le nombre de bombe adjacent/ fin de partie en cas de bombe sur la case

    Parameters
    ----------
    jeu : list
        la grille du jeu.
    n : int
        position dans la ligne.
    p : int
        position dans la colonne.

    Returns
    -------
    str ou int
        soit un "X" si la case est une bombe soit un integer representant le nombre de bombes adjacentes.

    '''
    assert type(n) and type(p) == int, "Type: les coordonnees de la case doivent etre des integer"
    if jeu[n][p].est_piegee()!=False:
        bombe=0
        if n==0 and p==0:#hg
            for i in range(2):
                for y in range(2):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        elif n==len(jeu)-1 and p==0:#bg
            for i in range(-1,1):
                for y in range(2):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        elif n==0 and p==len(jeu[0])-1:#hd
            for i in range(2):
                for y in range(-1,1):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        elif n==len(jeu)-1 and p==len(jeu[0])-1:#bd
            for i in range(-1,1):
                for y in range(-1,1):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        elif n==0:#h
            for i in range(2):
                for y in range(-1,2):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        elif n==len(jeu)-1:#b
            for i in range(-1,1):
                for y in range(-1,2):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        elif p==0:#g
            for i in range(-1,2):
                for y in range(2):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        elif p==len(jeu[0])-1:#d
            for i in range(-1,2):
                for y in range(-1,1):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1

        else:
            for i in range(-1,2):
                for y in range(-1,2):
                    if jeu[n+i][p+y].est_piegee()==False:
                        bombe+=1
        if bombe==0:
            bombe=''
        return bombe
    else:
        return False

def est_fini(jeu):
    '''
    test si le jeu est fini

    Parameters
    ----------
    jeu : list
        la grille du jeu.

    Returns
    -------
    fin : boolean
        le jeu est fini.

    '''
    fin=True
    for i in jeu:
        for y in i:
            if y!=False:
                fin=False
    return fin


def affiche(jeu):
    '''
    Affiche le quadrillage du jeu

    Parameters
    ----------
    jeu : list
        Tableau du jeu

    Returns
    -------
    None.

    '''
    for n in range(len(jeu)):
        for p in range(len(jeu[0])):
            can.create_rectangle(2+n*500/len(jeu),2+p*500/len(jeu[0]),2+(n+1)*500/len(jeu),2+(p+1)*500/len(jeu[0]))


def replay():
    '''
    Recommence une partie et remet a zero l'ancien jeu et l'affichage

    Returns
    -------
    None.

    '''
    global MEMO
    can.delete("all")
    cote=int(ent.get())
    bombe=int(ent2.get())
    jeu=genere_jeu(cote,cote,bombe)
    affiche(jeu)
    MEMO=[]
    can.bind("<Button-1>", lambda event: play(event,jeu))
    can.bind("<Button-3>", lambda event: drapo(event,jeu))


def drapo(event,jeu):
    '''
    Place un drapeau sur une case

    Parameters
    ----------
    event : tkinter.Event
        coordonées du clique
    jeu : list
        Tableau du jeu

    Returns
    -------
    None.

    '''
    global MEMO
    test=0
    coo=int(2+(event.x)//(502/int(ent.get())))-2 , int(2+(event.y)//(502/int(ent.get())))-2
    if coo not in MEMO:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text="X",fill="black",font=("Arial",15))
    else:
        actu=traitement_case(jeu,coo[0],coo[1])
        if actu!='' and actu==False:
            can.create_rectangle(2+coo[0]*500/int(ent.get()),2+coo[1]*500/int(ent.get()),2+(coo[0]+1)*500/int(ent.get()),2+(coo[1]+1)*500/int(ent.get()),fill="#ADD8E6")
        elif jeu[coo[0]][coo[1]].getval()==True:
            can.create_rectangle(2+coo[0]*500/int(ent.get()),2+coo[1]*500/int(ent.get()),2+(coo[0]+1)*500/int(ent.get()),2+(coo[1]+1)*500/int(ent.get()),fill="#ADD8E6")
        else:
            change((coo[0],coo[1]),"white",actu)
        test=1
    if test==1:
        MEMO.remove(coo)
    else:
        MEMO.append(coo)


def play(event,jeu):
    '''
    cette fonction lance le jeu et l'arrete'

    Parameters
    ----------
    event : tkinter.Event
        coordonées du clique
    jeu : list
        Tableau du jeu

    Returns
    -------
    None.

    '''
    coo=int(2+(event.x)//(502/int(ent.get())))-2 , int(2+(event.y)//(502/int(ent.get())))-2
    actu=traitement_case(jeu,coo[0],coo[1])
    if actu==False:
        reveal(jeu)
        can.create_text(250,250,text="U BAD >:(",font=('Arial',50),activefill="red2")
        can.unbind("<Button-1>")
        can.unbind("<Button-3>")
    else:
        if actu=='':
            propa(coo,jeu,[])
        else:
            change(coo,"white",actu)
            jeu[coo[0]][coo[1]].conversion()

    if test_fin(jeu):
        can.create_text(250,250,text="VICTORYY !!",font=('Arial',50),activefill="navy")
        can.unbind("<Button-1>")
        can.unbind("<Button-3>")


def propa(coo,jeu,liste=[]):
    '''
    Cette fonction gere la propagation des cases sans bombes alentour

    Parameters
    ----------
    coo : list
        coordonnees de la case
    jeu : list
        Tableau du jeu
    liste : list, optional
        Garde en memoire les differentes cases visitees. The default is [].

    Returns
    -------
    test : int
        nombre de bombe alentours

    '''
    n=coo[0]
    p=coo[1]
    test=traitement_case(jeu,n,p)
    jeu[n][p].conversion()
    if test!='' or coo in liste:
        return test

    else:
        liste.append(coo)
        if n==0 and p==0:#hg
            for i in range(2):
                for y in range(2):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)

        elif n==len(jeu)-1 and p==0:#bg
            for i in range(-1,1):
                for y in range(2):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)

        elif n==0 and p==len(jeu[0])-1:#hd
            for i in range(2):
                for y in range(-1,1):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)

        elif n==len(jeu)-1 and p==len(jeu[0])-1:#bd
            for i in range(-1,1):
                for y in range(-1,1):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)

        elif n==0:#h
            for i in range(2):
                for y in range(-1,2):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)

        elif n==len(jeu)-1:#b
            for i in range(-1,1):
                for y in range(-1,2):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)
        elif p==0:#g
            for i in range(-1,2):
                for y in range(2):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)

        elif p==len(jeu[0])-1:#d
            for i in range(-1,2):
                for y in range(-1,1):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)

        else:
            for i in range(-1,2):
                for y in range(-1,2):
                    if not(n+i==n and p+y==p):
                        change((n+i,p+y),"white",traitement_case(jeu,n+i,p+y))
                        propa((n+i,p+y),jeu,liste)


def change(coo,color,text=''):
    '''
    change l'apparence d'une case

    Parameters
    ----------
    coo : list
        coodronnees de la case
    color : str
        couleur du fond de la case
    text : str/int, optional
        Le nombre de bombe alentour ou l'absence de bombe. The default is ''.

    Returns
    -------
    None.

    '''
    can.create_rectangle(2+coo[0]*500/int(ent.get()),2+coo[1]*500/int(ent.get()),2+(coo[0]+1)*500/int(ent.get()),2+(coo[1]+1)*500/int(ent.get()),fill=color)
    if text==1:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="cyan",font=("Arial",15))
    elif text==2:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="green",font=("Arial",15))
    elif text==3:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="steel blue",font=("Arial",15))
    elif text==4:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="blue",font=("Arial",15))
    elif text==5:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="goldenrod",font=("Arial",15))
    elif text==6:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="orange",font=("Arial",15))
    elif text==7:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="red",font=("Arial",15))
    elif text==8:
        can.create_text((2+coo[0]*500/int(ent.get())+2+(coo[0]+1)*500/int(ent.get()))/2,(2+coo[1]*500/int(ent.get())+2+(coo[1]+1)*500/int(ent.get()))/2,text=str(text),fill="magenta",font=("Arial",15))


def reveal(jeu=[]):
    '''
    affiche l'entierete du jeu en cas de defaite

    Parameters
    ----------
    jeu : list, optional
        Tableau du jeu. The default is [].

    Returns
    -------
    None.

    '''
    if jeu==[]:
        return None
    for ind,i in enumerate(jeu):
        for ynd,y in enumerate(i):
            actu=traitement_case(jeu,ind,ynd)
            if y.est_piegee()==False:
                change((ind,ynd),"red")
            else:
                change((ind,ynd),"white",actu)


def test_fin(jeu):
    '''
    test si le jeu est fini

    Parameters
    ----------
    jeu : list
        Tableau du jeu

    Returns
    -------
    bool
        le jeu est fini ou non

    '''
    for ind,i in enumerate(jeu):
        for ynd,y in enumerate(i):
            if y.getval()==True:
                return False
    return True

#recuperation de la taille
text=Label(fen,text="Le nombre de cases de cote :")
text.grid(row=3)
ent=Entry(fen,width=50)
ent.grid(row=4)

#recuperation du nombre de bombe
text=Label(fen,text="Le nombre de bombes :")
text.grid(row=5)
ent2=Entry(fen,width=50)
ent2.grid(row=6)

#reset
reset=Button(fen,text="Play/Reset",command=replay)
reset.grid(row=7)

#destruction de la fenetre
quitte=Button(fen,text="Quitter",command=fen.destroy)
quitte.grid(row=8)


#print(traitement_case(genere_jeu(10, 10, 10), 10, 10))
fen.mainloop()