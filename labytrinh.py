import random as r
from tkinter import*
from turtle import*
fen=Tk()


class Case():
    def __init__(self,x,y,val,s=True,e=True,n=True,o=True):
        '''
        initialise une case

        Parameters
        ----------
        x : int
            position de la ligne dans la liste
        y : int
            position de la colonne dans la liste
        val : int
            valeur de la case
        s : bool, optional
            mur du bas. The default is True.
        e : bool, optional
            mur de droite. The default is True.
        n : bool, optional
            mur du haut. The default is True.
        o : bool, optional
            mur de gauche. The default is True.

        Returns
        -------
        None.

        '''
        self.x=x
        self.y=y
        self.val=val
        self.s=s
        self.e=e
        self.n=n
        self.o=o

    def get_val(self):
        return self.val

    def supprime_mur(self,other,hori,jeu):
        '''
        supprime les mur entre 2 cases

        Parameters
        ----------
        other : Case
            une case.
        hori : int
            l'orientation du mur.
        jeu : list
            le jeu.

        Returns
        -------
        None.

        '''
        if self.val!=other.val:
            if hori==0:
                self.s=False
                other.n=False
            elif hori==1:
                self.e=False
                other.o=False
            elif hori==2:
                self.n=False
                other.s=False
            elif hori==3:
                self.o=False
                other.e=False
            self.change(other,jeu)

    def change(self,other,jeu):
        '''
        change les valeurs de 2 cases, la plus petit sera appliqué a toutes
        les case portant la meme valeur que la plus eleve

        Parameters
        ----------
        other : Case
            une case.
        jeu : list
            le jeu.

        Returns
        -------
        None.

        '''
        mini,maxi=self.val,other.val
        if self.val>other.val:
            mini,maxi=other.val,self.val
            
        for i in jeu:
            for y in i:
                if y.val==maxi:
                    y.val=mini

        
    def mur(self):
        '''
        liste de tout les murs

        Returns
        -------
        list
            les murs d'une case.

        '''
        return [self.s,self.e,self.n,self.o]
        
    def carre_tk(self,c,can):
        '''
        represente une case dans le canevas

        Parameters
        ----------
        c : int
            cote d'une case.
        can : Canvas
            le canevas dans lequel on represente le labyrinthe.

        Returns
        -------
        None.

        '''
        if self.s==True:
            can.create_line(self.x+2,self.y+c+2,self.x+c+2,self.y+c+2)
        if self.e==True:
            can.create_line(self.x+c+2,self.y+2,self.x+c+2,self.y+c+2)
        if self.n==True:
            can.create_line(self.x+2,self.y+2,self.x+c+2,self.y+2)
        if self.o==True:
            can.create_line(self.x+2,self.y+2,self.x+2,self.y+c+2)
            
    def turtle(self,c):
        if self.s==True:
            penup()
            setpos(self.x+2-250,self.y+c+2-250)
            pendown()
            setpos(self.x+c+2-250,self.y+c+2-250)
            penup()
        if self.e==True:
            penup()
            setpos(self.x+c+2-250,self.y+2-250)
            pendown()
            setpos(self.x+c+2-250,self.y+c+2-250)
            penup()
        if self.n==True:
            penup()
            setpos(self.x+2-250,self.y+2-250)
            pendown()
            setpos(self.x+c+2-250,self.y+2-250)
            penup()
        if self.o==True:
            penup()
            setpos(self.x+2-250,self.y+2-250)
            pendown()
            setpos(self.x+2-250,self.y+c+2-250)
            penup()
    
    def __str__(self):
        return str(self.val)
    

def init_laby(n,p,c):
    '''
    initialise le labyrinthe, toute les cases on tous leurs murs

    Parameters
    ----------
    n : int
        nombre de case de large.
    p : int
        nombre de case de hauteur.
    c : int
        nombre de pixel de cote d'une case.

    Returns
    -------
    jeu : list
        le jeu.

    '''
    assert type(n) and type(p) == int, "Type: n et p doivent etre des integers"
    jeu=[]
    compte=0
    for y in range(n):
        ligne=[]
        y=y*c
        for x in range(p):
            x=x*c
            ligne.append(Case(x,y,compte))
            compte+=1
        jeu.append(ligne)
    return jeu

def mur_random(jeu):
    '''
    supprime un mur au hasard dans le jeu

    Parameters
    ----------
    jeu : list
        le jeu.

    Returns
    -------
    jeu : list
        le jeu.

    '''
    hori=r.randint(0,3)
    if len(jeu)==2 and len(jeu[0])==2:
        choix=r.randint(0,1)
        if hori==0:
            jeu[0][choix].supprime_mur(jeu[1][choix],hori,jeu)
        elif hori==1:
            jeu[choix][0].supprime_mur(jeu[choix][1],hori,jeu)
        elif hori==2:
            jeu[1][choix].supprime_mur(jeu[0][choix],hori,jeu)
        elif hori==3:
            jeu[choix][1].supprime_mur(jeu[choix][0],hori,jeu)
        return jeu
    
    elif len(jeu)==2:
        x=r.randint(0,1)
        y=r.random(0,len(jeu[0])-1)
        if hori==0:
            jeu[0][y].supprime_mur(jeu[1][y],hori,jeu)
            
        elif hori==1:
            if y!=len(jeu[0])-1:
                jeu[x][y].supprime_mur(jeu[x][y+1],hori,jeu)
                
        elif hori==2:
            jeu[1][y].supprime_mur(jeu[0][y],hori,jeu)
            
        elif hori==3:
            if y!=0:
                jeu[x][y].supprime_mur(jeu[x][y-1],hori,jeu)
        return jeu
            
    elif len(jeu[0])==2:
        x=r.randint(0,len(jeu)-1)
        y=r.randint(0,1)
        
        if hori==0:
            if x!=len(jeu)-1:
                print(jeu[x][y].mur(),jeu[x+1][y].mur(),"1",jeu[x][y].val,jeu[x+1][y].val)
                jeu[x][y].supprime_mur(jeu[x+1][y],hori,jeu)
                print(jeu[x][y].mur(),jeu[x+1][y].mur(),"2")
        elif hori==1:
            print(jeu[x][0].mur(),jeu[x][1].mur(),"1",jeu[x][0].val,jeu[x][1].val)
            jeu[x][0].supprime_mur(jeu[x][1],hori,jeu)
            print(jeu[x][0].mur(),jeu[x][1].mur(),"1",jeu[x][0].val,jeu[x][1].val,"2")
        elif hori==2:
            if x!=0:
                print(jeu[x][y].mur(),jeu[x-1][y].mur(),"1",jeu[x][y].val,jeu[x-1][y].val)
                jeu[x][y].supprime_mur(jeu[x-1][y],hori,jeu)
                print(jeu[x][y].mur(),jeu[x-1][y].mur(),"1",jeu[x][y].val,jeu[x-1][y].val,"2")
        elif hori==3:
            print(jeu[x][1].mur(),jeu[x][0].mur(),"1",jeu[x][1].val,jeu[x][0].val)
            jeu[x][1].supprime_mur(jeu[x][0],hori,jeu)
            print(jeu[x][1].mur(),jeu[x][0].mur(),"1",jeu[x][1].val,jeu[x][0].val,"2")
        return jeu
    
    else:
        x=r.randint(0,len(jeu)-1)
        if x==0 or x==len(jeu)-1:
            y=r.randint(1,len(jeu[0])-2)
        else:
            y=r.randint(0,len(jeu[0])-1)
        
        if x==0:
            if hori==0:
                jeu[x][y].supprime_mur(jeu[x+1][y],0,jeu)
            elif hori==1:
                jeu[x][y].supprime_mur(jeu[x][y+1],1,jeu)
            elif hori==3:
                jeu[x][y].supprime_mur(jeu[x][y-1],3,jeu)
            
        elif x==len(jeu)-1:
            if hori==1:
                jeu[x][y].supprime_mur(jeu[x][y+1],1,jeu)
            elif hori==2:
                jeu[x][y].supprime_mur(jeu[x-1][y],2,jeu)
            elif hori==3:
                jeu[x][y].supprime_mur(jeu[x][y-1],3,jeu)
            
        elif y==0:
            if hori==0:
                jeu[x][y].supprime_mur(jeu[x+1][y],0,jeu)
            elif hori==1:
                jeu[x][y].supprime_mur(jeu[x][y+1],1,jeu)
            elif hori==2:
                jeu[x][y].supprime_mur(jeu[x-1][y],2,jeu)
            
        elif y==len(jeu[0])-1:
            if hori==0:
                jeu[x][y].supprime_mur(jeu[x+1][y],0,jeu)
            elif hori==2:
                jeu[x][y].supprime_mur(jeu[x-1][y],2,jeu)
            elif hori==3:
                jeu[x][y].supprime_mur(jeu[x][y-1],3,jeu)
                
        elif hori==0:
            jeu[x][y].supprime_mur(jeu[x+1][y],0,jeu)
        elif hori==1:
            jeu[x][y].supprime_mur(jeu[x][y+1],1,jeu)
        elif hori==2:
            jeu[x][y].supprime_mur(jeu[x-1][y],2,jeu)
        elif hori==3:
            jeu[x][y].supprime_mur(jeu[x][y-1],3,jeu)
        
    return jeu

def test_fin(jeu):
    '''
    test si le labyrinthe est fini

    Parameters
    ----------
    jeu : list
        le jeu.

    Returns
    -------
    bool
        True le jeu est fini, False il ne l'est pas.

    '''
    for i in jeu:
        for y in i:
            if y.get_val()!=0:
                return False
    return True

def gener_laby(n,p,c,can,interface="tkinter"):
    '''
    genere un labyrinthe fonctionnel

    Parameters
    ----------
    n : int
        nombre de case de large.
    p : int
        nombre de case de hauteur.
    c : int
        nombre de pixel de cote d'une case.
    can : Canvas
        le canevas dans lequel le labyrinthe est represente.
    interface : str, optional
        la facon donc le labyrinthe est represente. The default is "tkinter".

    Returns
    -------
    jeu : list
        le jeu.

    '''
    jeu=init_laby(n,p,c)
    while test_fin(jeu)!=True:
        mur_random(jeu)
    test=[]
    compte=2
    while compte!=0:
        x=r.randint(0,len(jeu))
        y=r.randint(0,len(jeu[0]))
        if (x,y) not in test:
            if compte%2==0:
                compte-=1
                if interface=="tkinter":
                    debut_fin(x,y,c,"green",jeu,can)
                else:
                    debut_fin(x,y,c,"green",jeu,can,"turtle")
            else:
                compte-=1
                if interface=="tkinter":
                    debut_fin(x,y,c,"red",jeu,can)
                else:
                    debut_fin(x,y,c,"red",jeu,can,"turtle")
        test.append((x,y))
    test=[]
    return jeu
        
def debut_fin(x,y,c,couleur,jeu,can,interface="tkinter"):
    '''
    

    Parameters
    ----------
    x : int
        position dans les lignes.
    y : int
        position dans les colonnes.
    c : int
        nombre de pixel de cote d'une case.
    couleur : str
        la couleur de la case.
    jeu : list
        le jeu.
    can : Canvas
        le canevas.
    interface : str, optional
        la facon donc le labyrinthe est represente. The default is "tkinter".

    Returns
    -------
    None.

    '''
    if interface=="tkinter":
        can.create_oval(2+x*c,2+y*c,2+(x+1)*c,2+(y+1)*c,fill=couleur,outline="light blue")
    else:
        color(couleur,couleur)
        setpos(2+x*c-250-c//2,2+y*c-250)
        begin_fill()
        pendown()
        circle(c//2)
        penup()
        end_fill()
        pencolor("black")
        

def affiche(n,p,c,interface="tkinter"):
    '''
    

    Parameters
    ----------
    n : int
        nombre de case de large.
    p : int
        nombre de case de hauteur.
    c : int
        nombre de pixel de cote d'une case.
    interface : str, optional
        la facon donc le labyrinthe est represente. The default is "tkinter".

    Returns
    -------
    None.

    '''
    if interface=="turtle":
        can=Canvas(fen,width=n*c+2,height=p*c+2,bg="#ADD8E6")
        fen.destroy()
        penup()
        ht()
        speed(0)
        for i in gener_laby(p,n,c,can,"turtle"):
            for y in i:
                y.turtle(c)
        exitonclick()
    else:
        can=Canvas(fen,width=n*c+2,height=p*c+2,bg="#ADD8E6")
        can.pack()
        for i in gener_laby(p,n,c,can):
            for y in i:
                y.carre_tk(c,can)
        fen.mainloop()


            
affiche(2,2,20,"turtle")
            
        

        
        
        