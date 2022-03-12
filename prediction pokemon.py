import csv
pokemon=list(csv.reader(open("pokemon.csv",newline=''),delimiter=';'))

def euclidienne(st1,st2): 
    '''
    Parameters
    ----------
    st1 : liste d'int
        Une liste representant les stats d'un pokemon, liste d'integer
        
    st2 : liste d'int
        Une liste representant les stats d'un pokemon, liste d'integer
    Returns
    -------
    int
        Calcul la distance euclidienne, entre les 2 stats

    '''
    return round(((st1[0]-st2[0])**2+(st1[1]-st2[1])**2+(st1[2]-st2[2])**2+(st1[3]-st2[3])**2)**0.5,3)
    

def manhattan(st1,st2):
    '''
    Parameters
    ----------
    st1 : liste d'int
        Une liste representant les stats d'un pokemon, liste d'integer
        
    st2 : liste d'int
        Une liste representant les stats d'un pokemon, liste d'integer
    Returns
    -------
    int
        Calcul la distance grace a la methode de manhattan, entre les 2 stats

    '''
    return round(abs(st1[0]-st2[0])+abs(st1[1]-st2[1])+abs(st1[2]-st2[2])+abs(st1[3]-st2[3]),3)
        
def prediction(pokemon,stat,distance,kproche=7,affiche_plus_proche=False):
    '''
    Parameters
    ----------
    pokemon : Liste de liste
        liste d'une liste sous la forme [nom du pokemon (str),
        ses stats (tuple de 4 int pour la vie, attaque, defense, vistesse),
        le type du pokemon (str)]
    
    stat : tuple de 4 int 
        la vie, attaque, defense, vistesse
        
    distance : fonction 
        une fonction qui calcul une distance en 4 dimension
        
    kproche : int, optionnel
        Le nombre de proche voisins pris en compte
        Par default la valeur est 7.
    Returns
    -------
    stat_proche : str
        Un str representant le type le plus probable du pokemon avec les stats
        donner en parametre aisin que le type du pokemon aillant les stats le
        plus proche de celui donnee.
    '''
    
    # cree un dico avec comme cle la distance entre le nouveau pokemon et
    # chaque pokemon de la base de donnee, comme valeur le type du pokemon de
    # la base de donnee et ajoute la distance a 'fin'
    fin=[(distance(stat,[int(i[1]),int(i[2]),int(i[3]),int(i[4])]),i[5]) for i in pokemon[1:]]
        
    
    # tri la liste 'fin'
    fin.sort()
    

    # selectionne la precision et ajoute les type a 'type_proche'
    type_proche=[fin[i][1] for i in range(kproche)]
    
    
    # compte les occurence
    types=[(type_proche.count(i),i) for i in ["Eau","Feu","Plante","Electrik","Ténèbre","Psy","Vol","Roche","Insecte","Dragon","Poison","Combat","Normal","Spectre","Glace","Fée","Acier"]]
    
    
    # affiche les 'kproche' voisin les plus proche (optionnel)
    if affiche_plus_proche==True:
        print(fin[:kproche])
        
    return 'La moyenne des {} plus proche est de type: {}, et le plus proche est de type: {}'.format(str(kproche), str(sorted(types,key=lambda x:-x[0])[0][1]), str(type_proche[0]))


print(prediction(pokemon,(70,92,65,98),euclidienne,affiche_plus_proche=True),"\n")
print(prediction(pokemon,(70,92,65,98),manhattan),"\n")

print(prediction(pokemon,(75,98,63,101),euclidienne),"\n")
print(prediction(pokemon,(75,98,63,101),manhattan,affiche_plus_proche=True),"\n")

print("Ceci est le programme de Robin Fasseler")