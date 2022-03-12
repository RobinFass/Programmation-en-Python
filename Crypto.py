# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:42:41 2021

@author: fasseler_r
"""
'''importation des bibliotheques string et csv pour la liste des lettres de
l'alphabet et l'importation de fichier, ici ube liste de mots en francais'''
import string as st
import csv


'''importation et lecture du ficher "liste_francais"'''
att=list(csv.reader(open("liste_francais.txt",newline=''),delimiter=';'))


'''creation d'une liste globale (DICO) Ccontenant plus de 22,000 mots de la
langue francaise, tous mis en majuscule et les caractere spéciaux remplacer
par la lettre lui correspondant ou un espace'''
DICO=[]
for i in att:
    DICO.append(i[0].upper())


'''creation de dictionnaire globale, l'un avec comme clef le lettre
et comme valeure sa position dans l'alphabet (LETTRE) et l'autre l'inverse (POS)'''
LETTRE=dict()
POS=dict()
alphabet=[' ']+[i for i in st.ascii_uppercase]
for ind,i in enumerate(alphabet):
    LETTRE[i]=ind
    POS[ind]=i



def chiffrement(code,n):
    '''
    Ce programme permet de chiffre un code par la methode de cesar.

    Parameters
    ----------
    code : str
        le code a chiffrer.
    n : int
        Decalage du code.

    Returns
    -------
    fin : str
        le code chiffre.

    '''
    global LETTRE
    global POS
    fin=''

    for i in code.upper():

        if LETTRE[i]+n>len(LETTRE)-1:
            autre_n=n-len(LETTRE)
        elif LETTRE[i]+n<0:
            autre_n=n+len(LETTRE)
        else:
            autre_n=n

        fin+=POS[LETTRE[i]+autre_n]

    return fin

def dechiffrement(code,n):
    '''
    Ce programme permet de dechiffrer un code.

    Parameters
    ----------
    code : str
        Un code qui a ete chiffrer.
    n : int
        le decalage du chiffrement.

    Returns
    -------
    str
        le code dechiffrer.

    '''
    return chiffrement(code, -n)

def cassage(code):
    '''
    Ce programme permet de casser un code ecrit en francais, avec comme seul
    caractere les lettres de l'alphabet et l'espace.

    Parameters
    ----------
    code : str
        Un code chiffrer dans la langue francaise.

    Returns
    -------
    str
        le code dechiffré

    '''
    global DICO
    liste=[]

    for i in range(27):
        fin=dechiffrement(code, i).split()
        compte=0
        for y in fin:
            if y.upper() in DICO:
                compte+=1
        liste.append((compte,i))

    return dechiffrement(code,max(liste)[1])

#test de tout les decalage pour un code donne
for i in range(27):
    print(cassage(chiffrement("ce cassage de code fonctionne a merveille", i)),i)