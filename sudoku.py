def ligne(S,i):
    #Cette fonction prend en parametre une liste de nombres et un integer
    #Elle renvoie une liste de nombres, representant tout les nombres
    #contenue dans la ligne au rang 'i' sauf les '0'.
    fin=[]

    for nbr in S[i]:
        if nbr!=0:
            fin.append(nbr)

    return fin

def colonne(S,j):
    #Cette fonction prend en parametre une liste de nombres et un integer
    #Elle renvoie une liste de nombres, representant tout les nombres
    #contenue dans la colonne au rang 'j' sauf les '0'.
    fin=[]
    i=0

    while i<9:
        if S[i][j]!=0:
            fin.append(S[i][j])
        i+=1

    return fin

def bloc(S,i,j):
    #Cette fonction prend en parametre une liste de nombres et deux integer
    #Elle renvoie une liste de nombres, representant tout les nombres
    #contenue dans le bloc au coordonees (i,j) sauf les '0'.
    fin=[]
    finish=[]

    fin.append(S[i//3*3][j//3*3])
    fin.append(S[i//3*3][j//3*3+1])
    fin.append(S[i//3*3][j//3*3+2])
    fin.append(S[i//3*3+1][j//3*3])
    fin.append(S[i//3*3+1][j//3*3+1])
    fin.append(S[i//3*3+1][j//3*3+2])
    fin.append(S[i//3*3+2][j//3*3])
    fin.append(S[i//3*3+2][j//3*3+1])
    fin.append(S[i//3*3+2][j//3*3+2])

    for nbr in fin:
        if nbr!=0:
            finish.append(nbr)

    return finish


def possible(S,i,j):
    #Cette fonction prend en parametre une liste de nombres et deux integer
    #Elle renvoie une liste de nombres, representant tout les nombres
    #qui peuvent etre mis a la case de coordonees (i,j).
    test=[1,2,3,4,5,6,7,8,9]

    for loop in ligne(S,i):
        test.remove(loop)

    for loop2 in colonne(S,j):
        for lop2 in test:

            if lop2==loop2:
                test.remove(loop2)

    for loop3 in bloc(S,i,j):
        for lop3 in test:

            if lop3==loop3:
                test.remove(loop3)

    return test


def suivante(i,j):
    #Cette fonction prend en parametre deux integer
    #Elle renvoie un tuple correspondant au coordonees de la prochaine case
    if j == 8:
        return (i+1,0)

    else:
        return(i,j+1)


def solve(S,i,j):
    #Cette fonction prend en parametre une liste de nombre et deux nombre.
    #Elle renvoie 'False' pour passer a la case suivante, sinon elle renvoie
    #'True' quand la valeur de 'i' egal 9, cela signifie que le sudoku a ete
    #fait entierement
    if i==9:
        return True

    elif S[i][j]>0:
        next=suivante(i,j)
        return solve(S,next[0],next[1])

    for k in possible(S,i,j):
        S[i][j] = k
        next=suivante(i,j)

        if solve(S,next[0],next[1])==True:
            return True

    S[i][j] = 0
    return False


S=[[0,1,0,0,7,8,0,0,0],
   [0,8,0,0,4,0,9,0,0],
   [0,0,5,6,0,0,0,1,0],
   [1,0,0,0,6,0,0,0,5],
   [0,4,0,9,1,5,0,7,2],
   [0,6,7,0,8,0,4,0,0],
   [0,0,0,3,0,0,1,0,0],
   [0,7,0,8,9,0,0,2,3],
   [0,0,0,0,0,4,0,0,0]]

##S=[[9,0,0,0,8,0,3,0,0],
##[0,0,0,2,5,0,7,0,0],
##[0,2,0,3,0,0,0,0,4],
##[0,9,4,0,0,0,0,0,0],
##[0,0,0,7,3,0,5,6,0],
##[7,0,5,0,6,0,4,0,0],
##[0,0,7,8,0,3,9,0,0],
##[0,0,1,0,0,0,0,0,3],
##[3,0,0,0,0,0,0,0,2]]

##S=[[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,1,0,0,0,0,0,0],
##[0,0,0,0,0,0,2,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0],
##[0,0,0,0,0,0,0,0,0]]

if solve(S,0,0):
   for n in range(9):
    print(S[n])

