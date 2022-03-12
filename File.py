class File:
    #Class de type 'file' qui peut prendre une liste en parametre

     def __init__(self,liste=[]):
        #Initialisation de l'attribut 'liste'
        self.liste=liste

     def __str__(self):
        #Ne prend que l'instance courante en parametre, affiche 'liste' et
        #renvoie un str vide
        print(self.liste)
        return ""

     def __len__(self):
        #Ne prend que l'instance courante en parametre, renvoie la longueur de
        #la 'file'
        return len(self.liste)

     def defile(self):
        #Ne prend que l'instance courante en parametre, renvoie la premiere
        #valeur de la 'file' ou renvoie la 'file' en cas de 'liste' vide
        if self.liste==[]:
            return []
        return self.liste.pop(0)

     def enfile(self,ajoute):
        #Prend l'instance courante en parametre ainsi que la valeur a enfiler
        #Renvoie la nouvelle 'file"
        self.liste.append(ajoute)
        return File(self.liste)

     def est_vide(self):
        #Ne prend que l'instance courante en parametre, renvoie un booleen
        #selon que la 'liste' et vide ou non
        return self.liste==[]

     def suivant(self):
        #Ne prend que l'instance courante en parametre, et renvoie le premier
        #element de la 'file'
        return self.liste[0]

     def defilek(self,k):
        #Ne prend que l'instance courante en parametre, et renvoie le k-eme
        #element de la 'file'
        return self.liste[k]

     def affiche_file(self):
        #Ne prend que l'instance courante en parametre, insert "l'entree" et la
        #"sortie" de la 'file', l'affiche et remove "l'entree" et la "sorti"
        #afin de ne pas modifier la 'liste'
        self.liste.insert(0,"Sortie")
        self.liste.append("Entree")
        print(self.liste)
        self.liste.remove("Sortie")
        self.liste.remove("Entree")
        return None

##liste=File()
##a=0
##while a<15:
##    a+=1
##    liste.enfile(a)
##print(liste.est_vide())
##print(liste.suivant())
##liste.defile()
##liste.affiche_file()
##File([1,2,3,4]).enfile(5).affiche_file()
##print(liste.defilek(2))