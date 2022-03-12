class Noeud:
    #Classe de type 'Noeud' prenant en parametre la donné du noeud.
    #Les noeuds peuvent avoir des liens entre eux grace a la methode
    #'ajoute_fils' ce qui crée un graphe.
    def __init__(self,valeur):
        self.val=valeur
        self.fils=[]
        self.pere=None

    def __str__(self):
        return str(self.val)

    def montre_fils(self):
        for i in self.fils:
            print(i.val)

    def ajoute_fils(self,other):
        self.fils.append(other)
        other.pere=self
        return self.val, other.val

    def change_pere(self,other):
        self.pere=other.pere

    def get_pere(self):
        return self.pere

    def get_fils(self):
        return self.fils

    def get_val(self):
        return self.val

    def a_pour_descendant(self,other):
        for i in montre_deep(self):
            if i==other.val:
                return True
        return False

    def est_racine(self):
        return self.pere==None

    def est_feuille(self):
        return self.fils==[]

    def profondeur(self):
        if self.pere==None:
            return 0
        return 1+self.pere.profondeur()

def cherche_rec(racine,valeur):
    compte=0
    if racine.get_val()==valeur:
        compte=1
    if racine.get_fils()==[]:
        return compte
    for i in racine.get_fils():
        compte+=cherche_rec(i,valeur)
    return compte


def montre_deep(racine):
    if racine.get_fils()==[]:
       return [racine.get_val()]
    valeurs=[]
    for i in racine.get_fils():
        valeurs+=montre_deep(i)
    return [racine.get_val()]+valeurs

def montre_width(racine):
    test=[racine]
    for i in test:
        if i.get_fils()!=[]:
            for a in i.get_fils():
                test.append(a)
    fin=[]
    for b in test:
        fin.append(b.get_val())
    return fin

def longueur(racine):
    return len(montre_deep(racine))

def supprime_branche(racine,other):
    if other in racine.get_fils():
        racine.get_fils().remove(other)
    else:
        for i in racine.get_fils():
            i.supprime_branche(other)

def liste_branche(racine):
    fin=[]
    while racine.get_pere()!=None:
        fin.append(racine.get_val())
        racine=racine.get_pere()
    fin.append(racine.get_val())
    return fin

def supprime_noeud(racine,other):
    for ind,i in enumerate(other.get_fils()):
        i.change_pere(other.get_pere())
        other.get_pere().get_fils().insert(ind,i)
    if other in racine.get_fils():
        racine.get_fils().remove(other)
    else:
        for i in racine.get_fils():
            i.supprime_noeud(other)

def ancetre_commun(racine,other):
    #Cette fonction prend en parametre 2 Noeuds et une instance etant la
    #racine de l'arbre.
    #La fonction renvoie le plus proche ancetre commun des 2 variables
    #"other1" et "other2" entrés en parametre.
    branche1=liste_branche(racine)
    branche2=liste_branche(other)
    for boucle_b1 in branche1:
        for boucle_b2 in branche2:
            if boucle_b1==boucle_b2:
                return boucle_b2

def affiche(sel):
    fin=[]
    for i in sel:
        fin+=[i.get_val()]
    return fin

def traitement(racine):
    fin=[]
    test=montre_deep(racine)
    for i in test:
        fin.append(i**2)
    return fin

def affiche_arbre(racine,compte=0):
    print(compte*"-"+">"+str(racine.get_val()))
    for i in racine.get_fils():
        affiche_arbre(i,compte+1)

####Creation des noeuds####
a=Noeud(0) #racine de l'arbre

b=Noeud(1) #fils de a(0)
c=Noeud(2) #fils de a(0)
d=Noeud(3) #fils de a(0)

e=Noeud(4) #fils de b(1)
f=Noeud(5) #fils de b(1)

g=Noeud(6) #fils de c(2)
h=Noeud(7) #fils de c(2)

i=Noeud(8) #fils de d(3)
j=Noeud(9) #fils de d(3)

k=Noeud(10) #fils de e(4)

l=Noeud(11) #fils de k(10)
m=Noeud(12) #fils de k(10)

###creation de l'arbre####
a.ajoute_fils(b)
a.ajoute_fils(c)
a.ajoute_fils(d)

b.ajoute_fils(e)
b.ajoute_fils(f)

c.ajoute_fils(g)
c.ajoute_fils(h)

d.ajoute_fils(i)
d.ajoute_fils(j)

e.ajoute_fils(k)
k.ajoute_fils(l)
k.ajoute_fils(m)

####creation noeud/arbre annexe####
z=Noeud(666) #arbre annexe

####instruction sur l'arbre####
#supprime_noeud(a,b)

##print(montre_deep(a))
##print(montre_width(a))
##print(liste_branche(l))
##print(liste_branche(k))
##print(ancetre_commun(g,h)) #test normal
##print(ancetre_commun(l,k)) #'k' est l'ancetre de 'l'
##print(ancetre_commun(l,j)) #leurs ancetre commun est la racine
##print(ancetre_commun(l,z)) #'z' ne fais pas partie de l'arbre 'a'
##print(cherche_rec(a,0))
##print(traitement(a))
affiche_arbre(a)


####Expliquation d'ancetre commun####
#Initialisation:
"""
branche1: liste des peres du premier parametre entre
branche2: liste des peres du premier parametre entre
"""
#Algorithme:
"""
Pour boucle_b1 dans branche1
    Pour boucle_b2 dans branche2
        Si boucle_b1 est egal a boucle_b2 alors
            Renvoyer boucle_b2
        Fin Si
    Fin Pour
Fin Pour
"""

"""
On assimile a deux variable leurs liste de pere jusqu'a la racine, grace a la
fonction "liste_branche()" qui renvoie une liste de toutes les donnée des
noeuds pere du noeud entre en parametre.
Grace a ces listes il ne reste plus qu'a faire tourner de boucle ensemble
pour balayer toute les combinaisons de pere possible et si un meme pere est
present dans les 2 listes alors la fonction renverra la donnee du pere en
commun, dans le cas contraire elle renvoie "None" signifiant aucun ancetre
commun.
"""