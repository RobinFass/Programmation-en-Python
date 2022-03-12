import random
class Carte:
    #La class prend deux parameter le 'symbole' un str et le 'num'
    def __init__(self,symbole,num):
        #Prend un parametre deux variable un str 'symbole' et un int 'num'
        num=str(num)
        self.symbole=symbole
        self.numero=num.lower()

        if self.numero =="valet":
            self.numero=11
        elif self.numero=="dame":
            self.numero=12
        elif self.numero =="roi":
            self.numero=13
        elif self.numero=="1":
            self.numero=14

    def __str__(self):
        #Affiche le 'symbole' et le 'numero' de la carte
        #Renvoie un str vide
        print(self.symbole,self.numero)
        return ""

    def est_meilleure(self,other):
        #Prend deux 'Carte' en parametre et renvoie 'True' si le
        #premier 'numero' est plus grand sinon 'False'.
        return int(self.numero)>int(other.numero)

    def val(self):
        #Renvoie le 'numero' de la carte
        return int(self.numero)

    def est_egale(self,other):
        #Prend un parametre deux 'Carte' et renvoie 'True' ou 'False' suivant si
        #leure 'numero' sont egaux ou non.
        return self.numero==other.numero

class Jeu_Carte:
    #La class prend en parameter 'jeu' une liste de carte

    def __init__(self,jeu):
        #Prend en parametre une liste 'jeu'.
        self.jeu=jeu

    def __str__(self):
        #Affiche 'jeu' et renvoie un str vide.
        print(self.jeu)
        return ""

    def melange(self):
        #Prend en parametre un 'Jeu_Carte' et melange les positions des 'Carte'
        #le constituant
        #Renvoie 'jeu'
        fin=self.jeu
        self.jeu=[]
        for _ in range(len(fin)):
            att=fin.pop(0)

            for i in att:
                i=Carte(i[0],i[1])
                self.jeu.append(i)
            att=0
        random.shuffle(self.jeu)
        return self.jeu

    def distribue(self):
        #Prend en parametre un 'Jeu_Carte' et renvoie une liste la premiere
        #moitier du jeu et de la dexieme moitier dans cet ordre.
        jeu=self.melange()
        j1=jeu[len(jeu)//2:]
        j2=jeu[:len(jeu)//2]
        return [j1,j2]

    def __len__(self):
        #Renvoie un int, le nombre de 'Carte' dans 'jeu'.
        return len(self.jeu)

def couleur(liste,symbole):
    #prend une liste 'liste' et le symbole 'symbole' un str et ajouter
    #a tout les element le mot 'symbole'
    #Renvoie la liste avec le symbole a chaque valeur
    for index,val in enumerate(liste):
        liste.remove(val)
        liste.insert(index,(symbole,val))
    return liste


def cree(jeu):
    #prend en parametre 'jeu' un int
    #Renvoie une liste de tuple representant un jeu de carte

    fin=[]
    symb=["pique","coeur","carreau","trefle"]

    for i in range(4):
        if jeu==52:
            val=[2,3,4,5,6,7,8,9,10,'valet','dame','roi',1]

        elif jeu==32:
            val=[7,8,9,10,'valet','dame','roi',1]

        else:
            raise ValueError("Wrong value")

        fin.append((couleur(val,symb[i])))
    return fin

def partie(liste):
    #Prend en parametre un 'Jeu_Carte' constitué de 'Carte'
    #La fonction va utiliser les methodes des class 'Jeu_Carte' et 'Carte' et
    #ainsi simuler un partie d'une bataille fermee.
    #Renvoie 'nul' en cas d'egaliter sinon la fonction renvoie 'l1'.

    liste=liste.distribue()
    l1=liste.pop(0)
    l2=liste.pop(0)
    cote=[]
    compte=0
    while True:
            if compte==1000:
                return "nul"

            elif len(l1)<2 or len(l2)<2:
                return l1

            elif l1[0].est_egale(l2[0]):
                for i in range(2):
                    cote.append(l1[i])
                    cote.append(l2[i])
                for _ in range(2):
                    l1.remove(l1[0])
                    l2.remove(l2[0])


            elif l1[0].est_meilleure(l2[0]):
                while cote!=[]:
                    l1.append(cote.pop(0))
                l1.append(l1.pop(0))
                l1.append(l2.pop(0))

            else:
                while cote!=[]:
                    l2.append(cote.pop(0))
                l2.append(l2.pop(0))
                l2.append(l1.pop(0))

            compte+=1


def play(cartes):
    #Prend en parametre 'cartes' un int le nombre de cartes dans le jeu
    #En cas de victoire la fonction va attribue un boolen
    #representant le joueur 1.
    #Renvoie un booleen en cas de victoire et 'nul' en cas d'egalite.
    jeu=Jeu_Carte(cree(cartes))
    fin=partie(jeu)
    if len(fin)<2:
        return False
    elif fin=="nul":
        return "nul"
    else:
        return True


def resultat(tests=1000,jeu=32):
    #Prend deux parametre de type int, 'tests' un nombre represantant le nombre
    #de test fait avec la fonction 'play' et 'jeu' qui permet de determiner
    #le nombre de cartes du jeu, '64' pour tout le jeu et '32' pour de 7 a as
    #Renvoie les pourcentage de victoire et d'egalite.
    compte=0
    compte2=0
    egal=0
    for _ in range(tests):
        fin=play(jeu)
        if fin==False:
            compte2+=1
        elif fin==True:
            compte+=1
        else:
            egal+=1
    fin1=round(compte/tests*100,1)
    fin2=round(compte2/tests*100,1)
    fin3=round(egal/tests*100,1)
    return 'Player1 won '+str(fin1)+'%, player2 won '+str(fin2)+'% and '+str(fin3)+'% ties'

print(resultat())